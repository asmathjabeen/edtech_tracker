# 🎓 EdTech Assignment Tracker

A simple assignment tracking system built with **FastAPI** that allows **teachers** to post assignments and **students** to submit them — with file upload support, role-based authentication, and a clean UI.

---

## 🔧 Features

- 🧑‍🏫 **Teacher Role**:  
  - Create assignments  
  - View student submissions

- 🎓 **Student Role**:  
  - Submit assignments (with file upload support)

- 🔐 **Authentication**: JWT-based login and signup system

- 📁 **File Uploads**: Store and manage submissions with file handling

- 🖼️ **Frontend**: Minimal HTML interface to create/submit/view assignments

- 📜 **Swagger Docs**: Auto-generated at `/docs`

---

## 🛠️ Tech Stack

- FastAPI (Backend)
- SQLite (Database)
- HTML/CSS (Frontend)
- JWT (Authentication)
- Uvicorn (Server)

---

## 🚀 How to Run Locally

> 🧙‍♂️ Requires Python 3.9+ installed

```bash
# 1. Clone the repo
git clone https://github.com/your-username/edtech_tracker.git
cd edtech_tracker

# 2. Set up virtual environment
python -m venv venv
venv\Scripts\activate     # For Windows
# or
source venv/bin/activate  # For Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload
