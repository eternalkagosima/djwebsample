from django.db import models

class BTemp(models.Model):
	edate = models.DateField()
	btemp = models.FloatField(max_length=4)

	def __str__(self):
		return '<BTemp:edate=' + str(self.edate) + '(' + \
			'{:.1f}°C'.format(self.btemp) + ')>'