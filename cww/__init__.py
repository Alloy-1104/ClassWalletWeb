from flask import Flask
from flask import render_template, url_for, request, redirect, flash, session
from flask_migrate import Migrate

from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from cww.modules import gen_hash_id
from cww.modules import fetch_user_session

from cww.models import db, User, Wallet, Part, UserAffiliation

base_dir = os.path.dirname(__file__)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'cww.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.urandom(24)

migrate = Migrate(app, db)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_email):
    return User.query.get(user_email)

@app.route("/")
@login_required
def index():
    return render_template("index.html", user_name=session["user_name"], email=session["email"])

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("verify"))

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "GET":
        return render_template("verify.html")
    elif request.method == "POST":
        mode = request.form.get("submit")
        if mode == "register":
            email = request.form.get("email")
            user_name = request.form.get("user_name")
            password = request.form.get("password")
            password_hash = generate_password_hash(password, method="pbkdf2:sha256")
            user = User(email=email, user_name=user_name, password_hash=password_hash, authorized_name="")
            db.session.add(user)
            db.session.commit()
            login_user(user)
            fetch_user_session(user)
            return redirect("/")
        elif mode == "login":
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()
            if not user or not user.verify_password(password):
                flash("パスワードが違います")
                return redirect(url_for("verify"))
            flash("ログインしました")
            login_user(user)
            fetch_user_session(user)
            return redirect("/")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("verify"))

@app.route("/browse_db")
@login_required
def browse_db():
    if session["email"] == "crafter.alloy@gmail.com":
        db_data = {
            "users": User.query.all(),
            "wallets": Wallet.query.all(),
            "parts": Part.query.all(),
            "affiliations": UserAffiliation.query.all(),
        }
        return render_template("browse_db.html", **db_data)
    else:
        return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)

