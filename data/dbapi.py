from .__init__ import db
from .models import *
import logging
import config
import random

log = logging.getLogger('app')

def get_new_fortune(user_string):
	"""Get a new fortune for an entry or the same fortune if this entry has already been made.

	For a user_string, that is the name + birthdate, get a random fortune from the DB if the 
	same name and birthdate has never been entered or get the one that was selected last time.
	:params user_string: Name + birthdate, eg: johnsmith1970-01-10
	:returns: Fortune as string.
	"""
	used_fortune = UsedFortunes.query.filter(
		UsedFortunes.user_string == user_string).first()

	len_all_fortunes = len(AllFortunes.query.all())
	if used_fortune is None:
		new_used_fortune = UsedFortunes(user_string=user_string)
		new_fortune = AllFortunes.query.all()[random.randint(
			0, len_all_fortunes - 1)]
		new_used_fortune.fortune_text = new_fortune.fortune_text

		db.session.add(new_used_fortune)
		db.session.commit()

		return new_used_fortune.fortune_text

	else:
		return used_fortune.fortune_text