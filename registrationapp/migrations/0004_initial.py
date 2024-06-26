# Generated by Django 5.0.4 on 2024-04-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrationapp', '0003_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Student's first name.", max_length=100)),
                ('last_name', models.CharField(help_text="Student's last name.", max_length=100)),
                ('email', models.EmailField(help_text="Student's email address.", max_length=254)),
                ('mobile_number', models.CharField(help_text="Student's mobile number.", max_length=15)),
                ('address', models.CharField(help_text="Student's address.", max_length=200)),
                ('date_of_birth', models.DateField(help_text="Student's date of birth.")),
                ('nationality', models.CharField(help_text="Student's nationality.", max_length=100)),
                ('year', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], help_text="Student's academic year.")),
                ('department', models.CharField(help_text="Student's department.", max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], help_text="Student's gender", max_length=10)),
            ],
        ),
    ]
