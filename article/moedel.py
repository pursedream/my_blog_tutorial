from django.db import models
class Article(model.Model):
	title = model.CharField(max_length = 100)
	category = model.CharField(max_length =50 , blank =True)
	date_time = model.DateTimeField(auto_now_add = True)
	content  = model.TextField(blank = True , null = True)
def __unicode__(self):
	return self.title
def Meta:
	ordering  = ['-date_time']
