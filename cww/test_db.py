from cww.models import db, User, Wallet, Part, UserAffiliation
from cww.modules import gen_hash_id

user = User.query.get("test@test")
db.session.delete(user)
db.session.commit()

wallet_id = gen_hash_id()
wallet = Wallet(id=wallet_id, wallet_name="2-1")
db.session.add(wallet)

part_ex_id = gen_hash_id()
part_la_id = gen_hash_id()
part_ex = Part(id=part_ex_id, part_name="展示", parent_wallet_id=wallet_id)
part_la = Part(id=part_la_id, part_name="行燈", parent_wallet_id=wallet_id)
db.session.add(part_ex)
db.session.add(part_la)


user_affiliation_ex = UserAffiliation(id=gen_hash_id(), user_email="crafter.alloy@gmail.com", part_id=part_ex_id)
user_affiliation_la = UserAffiliation(id=gen_hash_id(), user_email="crafter.alloy@gmail.com", part_id=part_la_id)
db.session.add(user_affiliation_ex)
db.session.add(user_affiliation_la)

db.session.commit()
