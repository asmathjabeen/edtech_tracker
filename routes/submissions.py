from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import SubmissionCreate
from models import Submission, Assignment, User
from database import SessionLocal
from auth import verify_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/submissions")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def submit_assignment(submission: SubmissionCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_data = verify_token(token)
    if not user_data or user_data.get("role") != "student":
        raise HTTPException(status_code=403, detail="Only students can submit")

    student = db.query(User).filter(User.email == user_data["sub"]).first()
    new_submission = Submission(
        assignment_id=submission.assignment_id,
        student_id=student.id,
        content=submission.content
    )
    db.add(new_submission)
    db.commit()
    return {"message": "Submission successful"}

@router.get("/assignment/{assignment_id}")
def view_submissions(assignment_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_data = verify_token(token)
    if not user_data or user_data.get("role") != "teacher":
        raise HTTPException(status_code=403, detail="Only teachers can view submissions")

    submissions = db.query(Submission).filter(Submission.assignment_id == assignment_id).all()
    return submissions

