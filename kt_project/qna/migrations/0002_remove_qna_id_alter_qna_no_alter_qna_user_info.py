# Generated by Django 4.2.1 on 2023-06-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna',
            name='id',
        ),
        migrations.AlterField(
            model_name='qna',
            name='no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='qna',
            name='user_info',
            field=models.CharField(max_length=15),
        ),
    ]
