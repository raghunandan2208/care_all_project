from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Younger, Elder, Profile
from django import forms
from django.db import transaction

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']


class YoungerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_younger = True
        user.save()
        younger = Younger.objects.create(user=user)
        return user


class ElderSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_elder = True
        if commit:
            user.save()
        elder = Elder.objects.create(user=user)
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['bio']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['display_name', 'first_name', 'last_name', 'age', 'gender','location','mobile', 'email', 'about_me', 'address', 'image', "is_filled"]

    def clean_is_filled(self):
        is_filled = self.cleaned_data.get('is_filled')
        if not is_filled:
            raise forms.ValidationError('This field is required')
        return is_filled


class ContactForm(forms.Form):
    countries = [("IN","INDIA"),("CH","CHINA"),("US","UNITED STATES")]
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    phone = forms.RegexField(regex="^[6-9][0-9]{9}$", error_messages={"invalid":"Please provide valid Indian phone number"},required=False)
    message = forms.CharField(widget=forms.Textarea)
    city = forms.CharField()
    country = forms.ChoiceField(choices=countries)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if email == "" and phone == "":
            self.add_error("email","Atleast Email or Phone number should be provided")

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if "gmail" not in data:
            raise forms.ValidationError("Email domain must be gmail", code="invalid")
        else:
            return data
