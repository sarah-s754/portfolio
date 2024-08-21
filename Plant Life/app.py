import os
import threading
import time

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///plantlife.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show plant garden"""
    user_id = session["user_id"]

    garden = db.execute("SELECT * FROM garden WHERE user_id = ?", user_id)
    user_points = db.execute("SELECT points FROM users WHERE id = ?", user_id)[0]["points"]

    total_plant_points = sum(plant["price"] for plant in garden)
    total = user_points + total_plant_points

    return render_template("index.html", garden=garden, user_points=user_points, total=total)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure confirmation password was submitted
        elif not confirmation:
            return apology("must provide confirmation", 400)

        # Check password and confirmation match
        elif password != confirmation:
            return apology("Passwords do not match", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) > 0:
            return apology("Username already exists", 400)

        else:
            flash("Registered!")

            h_password = generate_password_hash(password)

            # Insert data into database
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, h_password)

            return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/info")
def info():
    """Show website information page"""
    return render_template("info.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """Change user password"""
    if request.method == "POST":
        user_id = session["user_id"]

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure password was submitted
        if not password:
            return apology("must provide password", 400)

        # Ensure confirmation password was submitted
        elif not confirmation:
            return apology("must provide confirmation", 400)

        # Check password and confirmation match
        elif password != confirmation:
            return apology("Passwords do not match", 400)

        else:
            flash("Password Changed!")

            h_password = generate_password_hash(password)

            # Insert data into database
            db.execute("UPDATE users SET hash = ? WHERE id = ?", h_password, user_id)

            return redirect("/")
    else:
        return render_template("profile.html")


@app.route("/log")
@login_required
def log():
    """Show gardening log"""
    user_id = session["user_id"]
    logs = db.execute("SELECT * FROM logs WHERE user_id = ?", user_id)

    return render_template("log.html", logs=logs)


@app.route("/guide")
@login_required
def guide():
    """Show table of plants"""
    user_id = session["user_id"]
    plants = db.execute("SELECT * FROM plants")

    return render_template("guide.html", plants=plants)


@app.route("/sow", methods=["GET", "POST"])
@login_required
def sow():
    """Trade points for plants"""

    plants = db.execute("SELECT name, price, image_filename FROM plants")

    if request.method == "POST":
        user_id = session["user_id"]
        plt_nm = request.form.get("name")
        num = request.form.get("number")

        # Check inputs
        try:
            num = int(num)
        except ValueError:
            return apology("Invalid number of plants", 400)

        if not plt_nm or num <= 0 or num % 1 != 0:
            return apology("Invalid symbol or number of plants", 400)

        # Check if the plant exists
        plant_info = next((plant for plant in plants if plant["name"] == plt_nm), None)
        if not plant_info:
            return apology("Invalid plant name", 400)

        plant_price = plant_info["price"]
        cost = plant_price * num

        # Check if the user has enough points
        user_points = db.execute("SELECT points FROM users WHERE id = ?", user_id)[0]["points"]
        if user_points < cost:
            return apology("Insufficient points", 400)

        flash("Plants bought!")

        # Get plant image filename
        image_filename = plant_info["image_filename"]

        # Repeat for the number of plants bought
        for _ in range(num):
            # Insert into the logs table
            db.execute("INSERT INTO logs (user_id, plant_name, quantity, price) VALUES (?, ?, ?, ?)", user_id, plt_nm, 1, plant_price)

            # Insert into the garden table
            db.execute("INSERT INTO garden (user_id, plant_name, price, plant_image_filename) VALUES (?, ?, ?, ?)", user_id, plt_nm, plant_price, image_filename)

        # Update user's points
        db.execute("UPDATE users SET points = points - ? WHERE id = ?", cost, user_id)

        return redirect("/")
    else:
        return render_template("sow.html", plants=plants)


@app.route("/water/<plant_id>", methods=["POST"])
@login_required
def water(plant_id):
    """Water a plant"""
    user_id = session["user_id"]

    flash("+1 Points!")

    # Update the last_watered column to the current timestamp
    db.execute("UPDATE garden SET status = ?, last_watered = ? WHERE id = ?", 'healthy', datetime.utcnow(), plant_id)

    # Give user points for water plant
    db.execute("UPDATE users SET points = points + 1 WHERE id = ?", user_id)

    return redirect("/")


# Ideas for implementation of timing functionality were sourced from ChatGPT
def update_plant_status():
    while True:
        print("Checking and updating plant status...")
        # Check and update plant status every minute
        plants = db.execute("SELECT * FROM garden WHERE status = 'healthy'")
        current_time = datetime.utcnow()

        print(f"Current Time: {current_time}")

        for plant in plants:
            last_watered = plant["last_watered"]

            if last_watered:
                last_watered = datetime.strptime(last_watered, '%Y-%m-%d %H:%M:%S')
                elapsed_time = current_time - last_watered

                print(f"Plant ID: {plant['id']}, Last Watered: {last_watered}, Elapsed Time: {elapsed_time}")

                if elapsed_time.total_seconds() > 120:
                    # Update the status to 'dry' if more than two minutes have passed
                    print(f"Updating status to 'dry' for Plant ID: {plant['id']}")
                    db.execute("UPDATE garden SET status = 'dry' WHERE id = ?", plant["id"])

        # Sleep for one minute before checking again
        time.sleep(60)


# Start the background task when the app is run
#if __name__ == '__main__':
thread = threading.Thread(target=update_plant_status)
thread.start()
app.run()
