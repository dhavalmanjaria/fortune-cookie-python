from .__init__ import db


class UsedFortunes(db.Model):
	row_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	user_string = db.Column(db.String())
	fortune_text = db.Column(db.String())


class AllFortunes(db.Model):
	row_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	fortune_text = db.Column(db.String())
