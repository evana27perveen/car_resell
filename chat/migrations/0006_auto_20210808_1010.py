# Generated by Django 3.2.6 on 2021-08-08 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellermessages',
            name='buyer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sellermessages',
            name='seller_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
