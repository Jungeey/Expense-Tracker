# Expense Tracker

A simple web-based Expense Tracker application developed using Python Flask and SQLite. It allows users to record expenses, view transaction history, and monitor their total spending.

## **Project Objective**

This project demonstrates web application development using Flask, Docker containerization, container image management using Azure Container Registry, and cloud deployment using Microsoft Azure App Service.

## Features

- Dashboard displaying total expenses and transaction count.
- Add expenses with name, amount, category, and date.
- View all recorded expenses.
- Automatic calculation of total spending.
- SQLite database for storing expense records.
- Docker containerization using a multi-stage Dockerfile.
- Cloud deployment using Microsoft Azure.

## Technologies Used

- Python 3.11
- Flask
- SQLite
- HTML5
- CSS3
- Docker
- Microsoft Azure
- Azure Container Registry (ACR)
- Azure App Service

## Project Structure

```text
ExpenseTracker/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   ├── add_expense.html
│   └── expenses.html
└── static/
    └── style.css
```


## **Run Locally**

### **1. Clone the repository**
```bash
git clone https://github.com/Jungeey/Expense-Tracker.git
cd Expense-Tracker
```

### **2. Create a virtual environment**
```bash
python3 -m venv venv
```

### **3. Activate the virtual environment**
```bash
source venv/bin/activate
```

### **4. Install dependencies**
```bash
pip install -r requirements.txt
```

### **5. Run the application**
```bash
python3 app.py
```

Open the application in your browser:

[http://localhost:5000](http://localhost:5000)

## **Docker Setup**

### **1. Build the Docker image**
```bash
docker build -t expensetracker:v1 .
```

### **2. Run the Docker container**
```bash
docker run -d -p 8080:80 --name expense-container expensetracker:v1
```

Open:

[http://localhost:8080](http://localhost:8080)

## **Azure Deployment**

The application is deployed on Microsoft Azure using Azure Container Registry and Azure App Service.

### **Azure Container Registry**

**Registry:** `sudipexpensetrackeracr2026`

**Docker Image:**
```text
sudipexpensetrackeracr2026.azurecr.io/expensetracker:v1
```

### **Live Application**

**Azure App Service:**

[https://sudip-expense-tracker-2026-cxcjdca9bxbkaeft.eastasia-01.azurewebsites.net/](https://sudip-expense-tracker-2026-cxcjdca9bxbkaeft.eastasia-01.azurewebsites.net/)

## **Author**

Sudip Jung Khatri
