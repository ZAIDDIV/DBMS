# 📋 Changelog — ElectroStock

All notable changes to this project are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standards.

> 🔴 **Live Build** — updated daily as features are pushed.

---

## [Unreleased] — In Progress
### 🔄 Currently Building
- Admin dashboard with real ElectroStock stats
- Product management module (add/edit/delete + images)
- Stock tracking + low stock alerts

---

## [Day 3] — 2026-04-28

### ✅ Added
- `role` field added to `Users` model — supports `developer`, `admin`, `cashier`
- Role-based login system fully implemented — each role redirects after login
- Helper methods added to Users model: `is_admin()`, `is_developer()`, `is_cashier()`
- Custom route decorators added: `@admin_required`, `@cashier_required`, `@developer_required`
- 3 system accounts created in MySQL: `developer`, `admin`, `cashier`
- Roles assigned in MySQL for all 3 accounts
- **ElectroStock sidebar** built and deployed — replaces CoreUI default menu completely
- Sidebar is **role-aware** — each user sees only what they're allowed to access:
  - Developer sees everything — Admin Panel + Cashier Panel + Developer tools
  - Admin sees Admin Panel + Cashier Panel
  - Cashier sees Cashier Panel only
- `current_user` passed to all templates for role-based rendering
- `pymysql.install_as_MySQLdb()` added to `apps/__init__.py` to fix MySQLdb import error
- `python-dotenv` installed — `.env` now loads properly on startup

### 🔧 Fixed
- Fixed `ModuleNotFoundError: No module named 'MySQLdb'` — resolved via pymysql as MySQLdb
- Fixed migrations folder missing — ran `flask db init` + `flask db migrate` + `flask db upgrade`
- Fixed Flask not detecting app — set `FLASK_APP=run.py` via `set` command

### 📝 Notes
- Sidebar uses Jinja2 `{% if current_user.role %}` conditions for dynamic rendering
- All 3 role accounts are live in MySQL `electrostock` database
- `.env` is gitignored — MySQL credentials never pushed to GitHub

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
