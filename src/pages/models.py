from django.db import models

from django.contrib.auth.models import User

import datetime

# Create your models here.

class JournalEntry(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	public = models.BooleanField(db_default=True)
	text = models.TextField()
	date = models.DateTimeField(default=datetime.datetime.now)

class PrivateView(models.Model):
	journal = models.OneToOneField(JournalEntry, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

