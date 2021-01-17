from django.forms import ModelForm
from .models import Items_data


class Items_data_Form(ModelForm):
	class Meta:
		model = Items_data
		fields = ('is_done' , )