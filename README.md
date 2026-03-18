# Crypto Tracker

A web application built with **Django** to track cryptocurrency prices in real time, displaying data for **Bitcoin**, **Solana**, and **Ethereum** in a clean and modern interface.

## Preview

The project shows three cards, one for each cryptocurrency, with:

- current price in USD
- short description of the coin
- historical chart with recent price variation
- modern dark UI

## Features

- Track **Bitcoin (BTC)**
- Track **Solana (SOL)**
- Track **Ethereum (ETH)**
- Display current price in USD
- Store price history with **SQLite**
- Show charts for recent price movements
- Built with Django templates, CSS, and Python backend

## Technologies Used

- **Python**
- **Django**
- **SQLite3**
- **HTML**
- **CSS**
- **JavaScript**
- **Chart.js**

## Project Structure

```bash
project/
├── home/
│   ├── migrations/
│   ├── static/
│   │   └── home/
│   │       └── home.css
│   ├── templates/
│   │   └── home/
│   │       └── home.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── project/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```
## How It Works

The application fetches cryptocurrency prices, processes the data in the Django backend, stores the values in a SQLite database, and renders them in the frontend using Django templates.

# The interface displays:

- the latest recorded price

- a short explanation of each cryptocurrency

- a line chart with recent price history

# Installation

Clone the repository:
```bash
git clone https://github.com/Josestmotter/Crypto_tracker.git
cd Crypto_tracker
```
# Create and activate a virtual environment:
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
```bash
python3 -m venv venv
source venv/bin/activate
```

# Install dependences
```bash
pip install -r requirements.txt
```

# Run migrations and start server 
```bash
python manage.py migrate
python manage.py runserver
```

# Open in browser

http://127.0.0.1:8000/

Author:
José Motter