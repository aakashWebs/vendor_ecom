Vendor eCommerce Platform - Django Project

Setup Instructions:
1. Create and activate a Python virtual environment.
2. Install dependencies: pip install -r requirements.txt
3. Run migrations: python manage.py migrate
4. Created a superuser: python manage.py createsuperuser with username and password(root:root)
5. Run the development server: python manage.py runserver
6. Access the site at http://127.0.0.1:8000/store/dashboard/ (login required)
7. Access the admin panel at http://127.0.0.1:8000/admin/
8. Added DRF for APIs 

Key Features:
- Vendor authentication using Django's built-in User model.
- Personalized dashboard for vendors to manage their own products and categories.
- Full CRUD functionality for categories and products with image upload and tag support.
- Custom admin panel with search and filter options for products and categories.
- Basic UI with class-based views for maintainability and code quality.
- Added bootstrap cdn for styling

Notes:
- Media files (product images) are served in development via Django.
- The project uses SQLite by default; you can configure other databases in settings.py.
