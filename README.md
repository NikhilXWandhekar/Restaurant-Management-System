🍽️ Restaurant Management System
📌 Overview
The Restaurant Management System is a full-stack web application built with React + Vite (frontend) and Django + Django REST Framework (backend).
It allows restaurant staff to manage restaurants, menus, tables, and orders with ease.
Key features include CRUD operations, real-time order status tracking, and a responsive UI for seamless use on desktops, tablets, and mobile devices.

🚀 Features
Restaurant Management: Add, edit, and delete restaurants.

Menu Management: Manage menu items with prices, categories, and availability.

Table Management: Track seating capacity and table status.

Order Handling: Create, update, and track orders in real time.

Responsive UI: Works across devices with a clean, modern design.

🛠 Tech Stack
Frontend

React + Vite

Axios (API calls)

TailwindCSS / Bootstrap (styling)

Backend

Django

Django REST Framework (DRF)

SQLite (default, easy to switch to PostgreSQL/MySQL)

📂 Project Structure
bash
Copy
Edit
restaurant-mgmt/
│
├── backend/
│   ├── restaurant/       # Django app
│   │   ├── models.py     # Restaurant, MenuItem, Table, Order, OrderItem
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── manage.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── pages/        # Home, Dashboard, Orders
│   │   ├── components/   # Reusable UI parts
│   │   ├── services/api.js
│   ├── package.json
│   ├── vite.config.js
⚙️ Installation & Setup
1️⃣ Backend Setup
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
2️⃣ Frontend Setup
bash
Copy
Edit
cd frontend
npm install
npm run dev
Visit: http://localhost:5173

🔄 How It Works
Admin/Manager creates a restaurant, sets up tables, and adds menu items.

Waiters create orders and assign them to tables.

Kitchen staff view and update order statuses.

Cashiers finalize bills and close orders.

Data is synced between React frontend and Django backend via REST APIs.

🛠 Future Improvements
🔐 JWT Authentication & Role-Based Access (Admin, Staff, Customer)

🌐 WebSocket-based real-time order updates

📊 Dashboard with sales & performance analytics

📱 Mobile app version using React Native

