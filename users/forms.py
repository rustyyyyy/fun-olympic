import re

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext as _
from pyexpat import model
from zxcvbn_password import zxcvbn
from zxcvbn_password.fields import PasswordConfirmationField, PasswordField
from django_countries.fields import CountryField

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone",
            "country",
        )

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "password_lower_alpha": _("The password should contain lower alphabet."),
        "password_upper_alpha": _("The password should contain upper alphabet."),
        "password_numeric": _("The password should contain numbers."),
        "password_special_char": _("The password should contain special character."),
        "not_strong": _("Please choose strong password."),
    }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )

        if not re.search("[a-z]", password1):
            raise forms.ValidationError(
                self.error_messages["password_lower_alpha"],
                code="password_lower_alpha",
            )

        if not re.search("[A-Z]", password1):
            raise forms.ValidationError(
                self.error_messages["password_upper_alpha"],
                code="password_upper_alpha",
            )

        if not re.search("[0-9]", password1):
            raise forms.ValidationError(
                self.error_messages["password_numeric"],
                code="password_numeric",
            )

        if not re.search("[$#@]", password1):
            raise forms.ValidationError(
                self.error_messages["password_special_char"],
                code="password_special_char",
            )

        if password1:
            score = zxcvbn(password1)["score"]
            if score < 3:
                raise forms.ValidationError(
                    self.error_messages["not_strong"],
                    code="not_strong",
                )

        return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )


class RegisterForm(forms.Form):
    password1 = PasswordField(label="Password")
    password2 = PasswordConfirmationField(label="Confirm Password")

    password1.widget.attrs.update(
        {"class": "form-control form-control-lg form-control-solid", "placeholder": ""}
    )
    password2.widget.attrs.update(
        {"class": "form-control form-control-lg form-control-solid", "placeholder": ""}
    )

class CountryForm(forms.Form):
    country = CountryField().formfield(label="Country")

    country.widget.attrs.update(
        {"class": "form-control form-control-lg form-control-solid mb-6", "placeholder": ""}
    )


gender_choices= (
    (0, ""),
    (1, "Male"),
    (2, "Female"),
)

class GenderForm(forms.Form):
    gender = forms.ChoiceField(choices = gender_choices)

    gender.widget.attrs.update(
        {"class": "form-control form-control-lg form-control-solid mb-6", "placeholder": ""}
    )
