# Generated by Django 3.2.6 on 2021-08-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_cars', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='year',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]