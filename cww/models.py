from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(UserMixin, db.Model):
  __tablename__ = "user"

  email = db.Column(db.String(160), primary_key=True, nullable=False)
  user_name = db.Column(db.String(40), nullable=False)
  password_hash = db.Column(db.String(200), nullable=False)
  authorized_name = db.Column(db.String(40), nullable=False)

  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')

  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def get_id(self):
    return self.email

class Wallet(db.Model):
  __tablename__ = "wallet"

  id = db.Column(db.String(8), primary_key=True, nullable=False)
  wallet_name = db.Column(db.String(8), nullable=False)

  parts = db.relationship("Part", backref="wallet", lazy=True)  

class Part(db.Model):
  __tablename__ = "part"

  id = db.Column(db.String(8), primary_key=True, nullable=False)
  part_name = db.Column(db.String(40), nullable=False)
  parent_wallet_id = db.Column(db.String(8), db.ForeignKey("wallet.id"), nullable=False)
  