
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db()
    total = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]
    count = conn.execute("SELECT COUNT(*) FROM expenses").fetchone()[0]
    conn.close()
    return render_template("index.html", total=total or 0, count=count)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        name = request.form["name"]
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]

        conn = get_db()
        conn.execute(
            "INSERT INTO expenses (name, amount, category, date) VALUES (?, ?, ?, ?)",
            (name, amount, category, date)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("view_expenses"))

    return render_template("add_expense.html")

@app.route("/expenses")
def view_expenses():
    conn = get_db()
    expenses = conn.execute("SELECT * FROM expenses ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("expenses.html", expenses=expenses)

def initialize_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    app.run(host="0.0.0.0", port=80, debug=False)
