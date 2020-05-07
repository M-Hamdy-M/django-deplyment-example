from django import forms
from django.contrib.auth.models import User
from firstapp.models import UserProfileInfo
from firstapp import models

from django.core import validators

class FormName(forms.ModelForm):
    class Meta:
        model = models.person
        fields = "__all__"

    # def clean(self):
    #     alldata = super().clean()
    #     email = alldata['email']
    #     vmail = alldata['vemail']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("please enter matched email!")
    #
    #     if email[-10:]!="@yahoo.com":
    #         raise forms.ValidationError("please enter a yahoo email! ")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site',)
        # fields = ('profile_pic', 'portfolio_site')

