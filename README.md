<div align="center">

<img src="https://img.shields.io/badge/ElectroStock-v1.0-blue?style=for-the-badge&logo=lightning&logoColor=white" />
<img src="https://img.shields.io/badge/Flask-2.2.5-black?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/CoreUI-Bootstrap5-purple?style=for-the-badge&logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

<br/><br/>

```
███████╗██╗     ███████╗ ██████╗████████╗██████╗  ██████╗ ███████╗████████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝
█████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║   ██║███████╗   ██║   ██║   ██║██║     █████╔╝ 
██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║   ██║╚════██║   ██║   ██║   ██║██║     ██╔═██╗ 
███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║╚██████╔╝███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗
╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝
```

### ⚡ Full-Stack Inventory Management System for Electronics & Electrical Retail Stores

> 🔴 **Live Build** — Code is pushed daily as features are developed. Watch it grow from zero to a fully working production system, one commit at a time.

</div>

---

## 📌 What Is ElectroStock?

**ElectroStock** is a complete, role-based inventory and billing management system built for small to medium electronics retail stores — think lights, fans, switches, wiring, and general electrical goods.

It is **not** a template. It is a **real working system** being built from scratch with a proper tech stack, clean architecture, and production-level thinking. Everything from stock management and billing to warranty tracking and customer history is handled inside one unified platform.

Built on top of **Flask + CoreUI Dashboard**, ElectroStock combines a beautiful Bootstrap 5 frontend with a powerful Python/MySQL backend — giving store owners and cashiers a fast, intuitive, and reliable system to run their business.

---

## 🧠 System Architecture

The system is split into two operational sides, with three distinct user roles controlling access at every level.

```
┌─────────────────────────────────────────────────────────┐
│                     ElectroStock                        │
├───────────────────────┬─────────────────────────────────┤
│      ADMIN SIDE       │        CASHIER SIDE             │
│  (Store Management)   │      (Counter / Sales)          │
├───────────────────────┼─────────────────────────────────┤
│ • Product Management  │ • Product Search                │
│ • Stock Control       │ • Quantity Entry                │
│ • Supplier Tracking   │ • Auto Bill Generation          │
│ • Warranty Dashboard  │ • Bill Append (same day)        │
│ • Customer Profiles   │ • Receipt Reprint               │
│ • Sales Reports       │ • Customer Lookup by Number     │
│ • Return/Reversals    │                                 │
└───────────────────────┴─────────────────────────────────┘
```

---

## 🔐 Role-Based Access Control

| Role | Access Level | Authentication |
|------|-------------|----------------|
| 👨‍💻 **Developer** | Full system + tracking + config | Hardcoded at deployment |
| 👑 **Admin** | Full store management | Password set by developer |
| 🧾 **Cashier** | Sales & billing only | Account assigned by admin |

> 🔒 Admin password is configured by the developer at deployment. Developer retains system-level access for maintenance and debugging at all times.

---

## ✨ Core Features

### 🛒 Billing System
- Auto-generates bills the moment cashier hits **Proceed**
- Create a **new bill** or **append to existing** for same-day returning customers
- **Customer number system** — enter a number, pull up full profile instantly
- Full bill history stored per customer
- PDF-ready receipt output

### 📦 Stock Management
- Real-time stock levels per product
- Admin can add stock, edit quantities, mark items as discontinued
- **Low-stock notifications** — know what to reorder before it runs out
- **Supplier management** — track who to order from and what payments are pending

### 👤 Customer System
- Every customer gets a **unique number** at first purchase
- Customer profile includes: name, contact, full purchase history
- Returning customers recognized instantly — even after months
- Pull up complete history in seconds

### 🛡️ Warranty Tracking
- Warranty expiry dates tracked automatically per product/sale
- Admin dashboard shows full warranty status at a glance
- **Warranty claims section** to manage and resolve disputes

### 🔄 Reversal Transactions
- Full return/reversal system from admin side
- Linked back to original bill and customer record
- **Stock auto-updates** on every reversal — no manual correction needed

### 🖼️ Edit Everywhere
- Images attachable to every product
- Every entity (product, customer, supplier, sale) has full edit capability
- Nothing is locked after creation

---

## 🏗️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python 3.x + Flask 2.2.5 | Core application logic |
| **Frontend** | CoreUI + Bootstrap 5 | Dashboard & UI components |
| **Database** | MySQL 8.0 | Primary data persistence |
| **ORM** | Flask-SQLAlchemy | Database modeling |
| **Auth** | Flask-Login + Sessions | Role-based authentication |
| **Migrations** | Flask-Migrate | Database version control |
| **Forms** | Flask-WTF | Secure form handling |
| **DB Connector** | PyMySQL | Python → MySQL bridge |
| **Config** | python-dotenv | Environment management |
| **Billing** | Python (PDF-ready) | Receipt & bill generation |
| **Deployment** | Docker ready | Production deployment |

---

## 📁 Project Structure

```
DBMS/  (ElectroStock)
│
├── apps/
│   ├── authentication/        # Login, register, session handling
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── models.py
│   │
│   ├── home/                  # Dashboard & main views
│   │   └── routes.py
│   │
│   ├── templates/             # HTML templates (CoreUI based)
│   │   ├── layouts/
│   │   ├── home/
│   │   └── authentication/
│   │
│   ├── static/                # CSS, JS, Images
│   └── config.py              # App configuration
│
├── .env                       # Environment variables (DB credentials etc.)
├── run.py                     # App entry point
├── requirements.txt           # Python dependencies
└── README.md
```

> 📌 Structure evolves daily as new modules are added

---

## 🗃️ Database Schema

**Database:** `electrostock` (MySQL 8.0)

| Table | Purpose |
|-------|---------|
| `users` | Developer, admin & cashier accounts with roles |
| `products` | Item catalog — name, price, category, image |
| `stock` | Real-time inventory levels per product |
| `suppliers` | Supplier info + payment status |
| `customers` | Customer profiles + unique customer number |
| `sales` | Every transaction on record |
| `sale_items` | Individual line items per sale |
| `bills` | Generated bill metadata |
| `warranties` | Warranty records per sale item with expiry |
| `reversals` | Return/refund transaction log |
| `stock_orders` | Reorder tracking per supplier |

---

## 📅 Build Progress

> 📋 For a detailed day-by-day breakdown of what was built and when, check the [CHANGELOG.md](./CHANGELOG.md)

| Module | Feature | Status |
|--------|---------|--------|
| ⚙️ **Setup** | Project setup + Flask CoreUI integration | ✅ Done |
| 🗄️ **Database** | MySQL connected + electrostock DB created | ✅ Done |
| 🔐 **Auth** | Role-based login — Dev / Admin / Cashier | 🔄 In Progress |
| 📦 **Products** | Add / edit / delete products + images | 🔜 Upcoming |
| 📊 **Stock** | Real-time tracking + low-stock alerts | 🔜 Upcoming |
| 🚚 **Suppliers** | Supplier management + payment tracking | 🔜 Upcoming |
| 🧾 **Billing** | Cashier panel + billing engine | 🔜 Upcoming |
| 🖨️ **Receipts** | Bill generation + PDF receipt printing | 🔜 Upcoming |
| 👤 **Customers** | Unique number system + customer profiles | 🔜 Upcoming |
| 📜 **History** | Purchase history + returning customer flow | 🔜 Upcoming |
| ➕ **Append Bill** | Add to existing bill for same-day returns | 🔜 Upcoming |
| 🛡️ **Warranty** | Warranty tracking dashboard | 🔜 Upcoming |
| 🔄 **Reversals** | Return / refund transaction system | 🔜 Upcoming |
| 📈 **Reports** | Admin reports & sales analytics | 🔜 Upcoming |
| 🧪 **Polish** | Testing, bug fixes & final polish | 🔜 Upcoming |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- MySQL 8.0
- Git

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/ZAIDDIV/DBMS.git

# 2. Navigate into it
cd DBMS

# 3. Install dependencies
pip install Flask==2.2.5 Werkzeug==2.2.3 Flask-SQLAlchemy Flask-Login flask-migrate flask-wtf email-validator pymysql cryptography

# 4. Set up your environment file
# Edit .env with your MySQL credentials:
# DB_ENGINE=mysql
# DB_NAME=electrostock
# DB_HOST=localhost
# DB_PORT=3306
# DB_USERNAME=root
# DB_PASS=yourpassword

# 5. Create the database in MySQL
mysql -u root -p
CREATE DATABASE electrostock;
exit

# 6. Run the app
python run.py
```

Then open your browser at `http://127.0.0.1:5000` 🚀

---

## 🙋 About the Developer

**Built by ZAIDDIV** — learning by building, one commit at a time.

> Not following tutorials. Not copying projects. Building something real, from scratch, that could actually be sold and deployed in a real store.

---

## 📜 License

MIT License — free to use, fork, and learn from.

---

<div align="center">

⭐ **Star this repo if you're following the journey!**

`Built with 🔥 by ZAIDDIV`

</div>