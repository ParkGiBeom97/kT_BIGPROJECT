# Generated by Django 4.2.1 on 2023-06-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pill_img_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_seq', models.CharField(max_length=50)),
                ('dl_name', models.CharField(max_length=50)),
                ('img_key', models.CharField(max_length=500)),
                ('drug_shape', models.CharField(max_length=50)),
                ('print_front', models.CharField(max_length=50)),
                ('print_back', models.CharField(max_length=50)),
                ('color_class1', models.CharField(max_length=50)),
                ('color_class2', models.CharField(max_length=50)),
            ],
        ),
    ]