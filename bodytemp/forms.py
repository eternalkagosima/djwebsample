from django import forms
from django.db.models.fields import FloatField
from django.forms import widgets
from .models import BTemp

class BTForm(forms.ModelForm):
	class Meta:
		model = BTemp
		fields = ['edate', 'btemp']
		widgets = {
			'edate': forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
			'btemp': forms.NumberInput(attrs={'class':'form-control','placeholder':'36.7(小数点1位まで)'}),
		}