from django import forms
from .models import Student
from django.core.exceptions import ValidationError

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            raise ValidationError('Please enter a valid mobile number with exactly 10 digits.')
        if Student.objects.filter(mobile_number=mobile_number).exists():
            raise ValidationError('This mobile number is already registered.')
        return mobile_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email or (not email.endswith(".com") and not email.endswith(".in")):
            raise ValidationError('Please enter a valid email address ending with ".com" or ".in".')
        if Student.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        for field_name, field_value in cleaned_data.items():
            if not field_value:
                raise ValidationError(f'{field_name.capitalize()} is required.')
        return cleaned_data
