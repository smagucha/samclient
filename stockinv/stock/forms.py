from django.forms import ModelForm
from .models import stock

class productform(ModelForm):
	class Meta:
		model= stock
		fields='__all__'