# Generated by Django 5.0.6 on 2024-05-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pastebin_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plaintext",
            name="expiry",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="expires in"
            ),
        ),
    ]