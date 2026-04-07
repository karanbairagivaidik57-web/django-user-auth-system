# Django User Authentication System with MySQL

A robust and secure User Authentication System built with **Django** and **MySQL (Aiven Cloud)**. This project features user registration, login, logout, and a protected dashboard, following industry-standard security practices.

## 🚀 Features
* **User Registration:** New users can create an account.
* **Secure Login:** Authentication with password hashing.
* **Protected Dashboard:** Only logged-in users can access the dashboard.
* **Logout:** Securely end user sessions.
* **Cloud Database:** Integrated with **MySQL via Aiven Cloud**.
* **Security Focused:** Sensitive credentials (like Database Passwords) are managed using Environment Variables.

## 🛠️ Tech Stack
* **Backend:** Django (Python)
* **Database:** MySQL (Aiven)
* **Frontend:** HTML5, CSS3
* **Deployment:** Render

## ⚙️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/karanbairagivaidik57-web/django-user-auth-system.git](https://github.com/karanbairagivaidik57-web/django-user-auth-system.git)
    cd django-user-auth-system
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file or set the following variable in your environment:
    * `DB_PASSWORD`: Your MySQL Database password.

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the server:**
    ```bash
    python manage.py runserver
    ```

## 🌐 Live Demo
The project is deployed on Render:[https://django-auth-karan.onrender.com]

## 👨‍💻 Author
**Karan Bairagi**
* GitHub: [@karanbairagivaidik57-web](https://github.com/karanbairagivaidik57-web)
