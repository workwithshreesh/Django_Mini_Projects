# Generated by Django 4.2.11 on 2024-05-26 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("guestbook_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guestbookentry",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
