from flask import session
from cww.models import db, User, Part, Wallet, UserAffiliation

from random import choices
from json import loads, dumps


ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SPELLS = ALPHABETS + NUMBERS
def gen_hash_id():
  length = 8
  return "".join(choices(SPELLS, k=length))

def fetch_user_session(user_object):
  session["user_name"] = user_object.user_name
  session["email"] = user_object.email

