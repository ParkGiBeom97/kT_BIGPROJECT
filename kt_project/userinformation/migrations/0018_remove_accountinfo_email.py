# Generated by Django 4.2.2 on 2023-06-25 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userinformation", "0017_alter_accountinfo_disease"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="accountinfo",
            name="email",
        ),
    ]
