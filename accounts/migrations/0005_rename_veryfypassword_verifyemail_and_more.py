# Generated by Django 4.1.3 on 2022-11-16 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_verifymobile_date_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VeryFyPassword',
            new_name='VerifyEmail',
        ),
        migrations.RenameField(
            model_name='verifyemail',
            old_name='new_password',
            new_name='new_email',
        ),
        migrations.RenameField(
            model_name='verifyemail',
            old_name='old_password',
            new_name='old_email',
        ),
    ]
