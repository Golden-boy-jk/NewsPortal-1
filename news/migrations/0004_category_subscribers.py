# Generated by Django 5.1.4 on 2025-02-22 13:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_alter_post_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                related_name="subscribed_categories",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
