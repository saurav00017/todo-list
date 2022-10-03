from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	#owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'own',default = '',null=True)
	#tid = models.IntegerField(primary_key = True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	task = models.CharField(max_length = 100,null=True)
	dt = models.DateTimeField(auto_now_add = True,null=True)

	def __str__(self):
		return self.task