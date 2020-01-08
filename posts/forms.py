from django import forms
from django.forms import ModelForm
from .models import Subscriber


class Subscribe(ModelForm):
	def __init__(self, *args, **kwargs):
		super(Subscribe, self).__init__(*args, **kwargs)
		self.fields['code'].required = False
	class Meta:
		model = Subscriber
		fields = ['name', 'code', 'email']
		widgets = {
		'code': forms.HiddenInput(),
		}

class Unsubscribe(ModelForm):
	class Meta:
		model = Subscriber
		fields = ['subscribed', 'code', 'email']
		widgets = {
		'code': forms.HiddenInput(),
		'email': forms.HiddenInput(),
		}

