# Generated by Django 4.2.1 on 2023-06-07 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinformation', '0004_user_info_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('뉴스', models.CharField(max_length=300)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinformation.user_info')),
            ],
        ),
    ]