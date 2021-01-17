from django.db import models



class Items_data(models.Model):
	name = models.CharField(max_length=30 )
	is_done = models.BooleanField( default=False )
	date_time = models.DateTimeField( auto_now_add=True )
	def __str__(self):
		if not self.is_done :return f'Name : {self.name} Completed : No'
		else : return f'Name : {self.name} Completed : Yes'