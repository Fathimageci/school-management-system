# SCHOOL-MANAGEMENT-SYSTEM

## Project Description
This project is a School Management System built with Django RestFramework.It provides a comprehensive platform for managing student details,library borrowing history,and fee records.The system implements role-based access control(RBAC) with seperate logins for three user roles:Admin,Librarian,office Staff.Each role has specific permissions ensuring secure and controlled access to different functionalities.
### Key Features:
- **Authentication:** Secure login using Django's authentication framework.
- **Admin Dashboard:** Comprehensive control over accounts and records.
- **Office Staff Dashboard:** Manage student details and fees history,can view library history.
- **Librarian Dashboard:** Access to library history and student details (view-only).
- **CRUD Operations:** Manage student details, library records, and fees history.
- **Role-Based Access Control:** Permissions tailored to user roles.

---
## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.9 or higher
- Django 4.x or higher
- SQLite (default) or PostgreSQL for production

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Fathimageci/school-management-system.git
   cd school-management-system
