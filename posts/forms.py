from django import forms
from django.forms import ModelForm
from .models import Subscriber


class SubscribeForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(SubscribeForm, self).__init__(*args, **kwargs)
		self.fields['code'].required = False
		self.fields['email'].required = True
	class Meta:
		model = Subscriber
		fields = ['name', 'code', 'email']
		widgets = {
		'code': forms.HiddenInput(),
		}

class UnsubscribeForm(ModelForm):
	class Meta:
		model = Subscriber
		fields = ['subscribed', 'code', 'email']
		widgets = {
		'code': forms.HiddenInput(),
		'email': forms.HiddenInput(),
		}

