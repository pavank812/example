from mongoapp.models import Create
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user
"""
class StringListField(forms.CharField):
	def prepare_value(self, value):
		return ', '.join(value)

	def to_python(self, value):
		if not value:
			return []
		return [item.strip() for item in value.split(',')]
"""
class CreateForm(forms.ModelForm):

	class Meta:
		model = Create
		fields = ('FirstName','LastName','Email')
