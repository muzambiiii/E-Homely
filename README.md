# 🏠 E-Homely — Online Food Ordering System

A **Django-based food ordering web application** built for a home-style canteen / mess. Customers browse a meal-wise menu, add dishes to a cart, pay the full amount online via **Razorpay**, and receive a **4-digit token number** to collect their order at the counter. Staff manage order status through a dedicated kitchen dashboard.

---

## ✨ Features

### 👤 Customer Side
- **Meal-wise Menu** — separate Breakfast (7–10:30 AM), Lunch (12–3 PM), and Dinner (7–10 PM) sections; dishes are shown only during their serving window
- **Live Stock Check** — dishes marked out-of-stock by staff are hidden from the cart automatically
- **Cart & Checkout** — browser-side cart persisted via `localStorage`; phone number normalisation (handles `91-` prefix, leading `0`, etc.)
- **Online Payment** — full 100 % advance collected through **Razorpay**; payment confirmed by both callback and webhook so no payment is lost even if the tab closes
- **Token Page** — after payment the customer receives a unique 4-digit token; the page polls the server every few seconds and updates the status live (New → Preparing → Ready → Picked Up)
- **Order Cancellation** — customers can cancel their own order while it is still in `new` or `out_of_stock` status
- **AI Butler Chatbot** — a conversational assistant that answers menu questions using live stock data
- **About & Location Pages** — restaurant info and an embedded map/location view

### 🍳 Staff Side
- **Kitchen Dashboard** (`/staff/`) — live list of all open paid orders; staff can advance statuses (New → Preparing → Ready → Picked Up) or mark as Cancelled / Out-of-stock
- **Menu Management** (`/staff/menu/`) — toggle individual dishes in/out of stock in real time
- **Admin Panel** (`/admin/`) — full Django admin for dishes, orders, and site settings (e.g. open/close ordering site-wide)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3 · Django 4+ |
| Database | SQLite (dev) — swap for PostgreSQL in production |
| Payments | Razorpay (REST API + Webhook) |
| Frontend | Vanilla HTML / CSS / JS (no framework) |
| Hosting | Render / any WSGI host |

---

## 📁 Project Structure

```
homelyy/                   ← project root
├── config/                ← Django project settings & root URL conf
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── orders/                ← sole Django app
│   ├── models.py          ← Dish, Order, OrderItem, SiteSetting
│   ├── views.py           ← all customer & staff views
│   ├── urls.py            ← URL routing
│   ├── chatbot.py         ← AI butler chatbot logic
│   ├── payments.py        ← Razorpay integration helpers
│   ├── admin.py           ← Django admin configuration
│   ├── static/orders/     ← CSS, JS, images, favicons
│   └── templates/orders/  ← HTML templates
│       ├── base.html
│       ├── home.html      ← landing / menu overview
│       ├── menu.html      ← per-meal dish listing
│       ├── checkout.html
│       ├── pay.html       ← Razorpay payment page
│       ├── token.html     ← post-payment token page
│       ├── staff.html     ← kitchen order dashboard
│       ├── staff_menu.html← stock management
│       ├── chatbot.html
│       ├── about.html
│       └── location.html
├── manage.py
├── db.sqlite3             ← dev database (not committed)
└── requirements.txt
```

---

## 🚀 Getting Started (Local Development)

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repo
```bash
git clone https://github.com/jerin-jaison/E-Homely.git
cd E-Homely
```

### 2. Create & activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations & create a superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** for the customer site and **http://127.0.0.1:8000/admin/** for the Django admin.

> **Note:** In development mode (`DJANGO_DEBUG=1`) Razorpay keys are not required. The checkout page shows a "Demo Pay" button that simulates a successful payment without hitting any real API.

---

## ⚙️ Environment Variables

Set these in your hosting environment (e.g. Render → Environment tab):

| Variable | Description | Default (dev) |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key | insecure dev value |
| `DJANGO_DEBUG` | `1` = debug on, `0` = production | `1` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts | `*` |
| `DJANGO_CSRF_ORIGINS` | Comma-separated trusted origins (HTTPS) | _(empty)_ |
| `RAZORPAY_KEY_ID` | Razorpay live/test key ID | _(empty — disables payment)_ |
| `RAZORPAY_KEY_SECRET` | Razorpay key secret | _(empty)_ |
| `RAZORPAY_WEBHOOK_SECRET` | Razorpay webhook signing secret | _(empty)_ |

---

## 💳 Razorpay Setup

1. Sign up at [razorpay.com](https://razorpay.com) and get your API keys from **Account & Settings → API Keys**.
2. Set `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET` as environment variables.
3. Create a webhook in the Razorpay dashboard pointing to `https://<your-domain>/payment/webhook/` and subscribe to the `payment.captured` event. Copy the **Webhook Secret** into `RAZORPAY_WEBHOOK_SECRET`.

---

## 📌 Key URLs

| URL | Purpose |
|---|---|
| `/` | Home — meal categories |
| `/menu/<breakfast\|lunch\|dinner>/` | Per-meal dish list |
| `/checkout/` | Cart checkout form |
| `/pay/<pk>/` | Razorpay payment page |
| `/order/<pk>/` | Token / order status page |
| `/chatbot/` | AI butler chatbot |
| `/about/` | About the restaurant |
| `/location/` | Location / map page |
| `/staff/` | Kitchen order dashboard (login required) |
| `/staff/menu/` | Live stock toggle (login required) |
| `/admin/` | Django admin |

---

## 🗺️ Order Flow

```
Customer browses menu
        ↓
  Adds dishes to cart
        ↓
  Fills checkout form (name + phone)
        ↓
  Razorpay payment (100% advance)
        ↓
  Token page — 4-digit token shown
        ↓
  Kitchen updates status: New → Preparing → Ready
        ↓
  Customer collects order at counter
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is for personal / educational use. Feel free to adapt it for your own canteen or mess.
