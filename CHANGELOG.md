# 📋 Changelog — ElectroStock

All notable changes to this project are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standards.

> 🔴 **Live Build** — updated daily as features are pushed.

---

## [Unreleased] — In Progress
### 🔄 Currently Building
- Role-based login system (Developer / Admin / Cashier)
- Custom sidebar navigation for ElectroStock modules
- Admin dashboard with real ElectroStock stats

---

## [Day 2] — 2026-04-17

### ✅ Added
- MySQL 8.0 installed and configured on local machine
- `electrostock` database created in MySQL
- Flask app successfully connected to MySQL using PyMySQL
- `.env` file configured with MySQL credentials (DB_ENGINE, DB_NAME, DB_HOST, DB_PORT, DB_USERNAME, DB_PASS)
- Installed Python packages: `pymysql`, `cryptography`

### 🔧 Fixed
- Resolved `flask_minify` incompatibility with Python 3.13 — commented out Flask-Minify from `run.py`
- Fixed `before_first_request` AttributeError by downgrading Flask to `2.2.5` and Werkzeug to `2.2.3`
- Fixed `ModuleNotFoundError: No module named 'flask_wtf'` — installed `flask-wtf`
- Fixed MySQL PATH issue on Windows — added MySQL bin to system PATH via `setx`

### 📝 Notes
- MySQL root credentials stored securely in `.env` file
- `.env` is gitignored — never pushed to GitHub

---

## [Day 1] — 2026-04-14

### ✅ Added
- Project initialized — DBMS folder set up on local machine
- Flask CoreUI open-source starter cloned into project root
- Bootstrap 5 + CoreUI dashboard running locally at `http://127.0.0.1:5000`
- Login & Register pages live and functional
- Session-based authentication working out of the box
- SQLite default database connected (temporary — replaced by MySQL in Day 2)
- Blueprint pattern confirmed — ready for ElectroStock module structure
- User account registered and dashboard accessible
- Installed core dependencies: `Flask`, `Flask-SQLAlchemy`, `Flask-Login`, `flask-migrate`, `flask-wtf`, `email-validator`

### 📝 Notes
- Decided to use Flask CoreUI as the frontend base instead of building CLI from scratch
- This gives us a production-ready Bootstrap dashboard to build ElectroStock on top of
- Old DBMS folder cleared — fresh start with Flask architecture
- `flask_minify` skipped due to Python 3.13 `cgi` module removal — not needed in development

---

## [Day 0] — 2026-04-13 — Project Planning

### ✅ Added
- ElectroStock concept finalized
- Full system design documented:
  - Two sides: Admin & Cashier
  - Three roles: Developer, Admin, Cashier
  - Core modules: Stock, Billing, Customers, Suppliers, Warranty, Reversals
- Database schema planned (10 core tables)
- Tech stack decided: Python + Flask + MySQL + CoreUI
- GitHub repository created: `github.com/ZAIDDIV/DBMS`
- README.md written with full project overview and daily build log

---

## 🗺️ Upcoming

| Day | Planned Feature |
|-----|----------------|
| Day 3 | Role-based login — Dev / Admin / Cashier |
| Day 4 | Product management — add / edit / delete + images |
| Day 5 | Stock tracking + low-stock alerts |
| Day 6 | Supplier management + payment tracking |
| Day 7 | Cashier panel + billing engine |
| Day 8 | Bill generation + PDF receipt printing |
| Day 9 | Customer number system + profiles |
| Day 10 | Purchase history + returning customer flow |
| Day 11 | Append-to-bill for same-day returns |
| Day 12 | Warranty tracking dashboard |
| Day 13 | Reversal / return transaction system |
| Day 14 | Admin reports & sales analytics |
| Day 15 | Testing, bug fixes & final polish |

---

<div align="center">

`Built with 🔥 by ZAIDDIV — one commit at a time`

</div>