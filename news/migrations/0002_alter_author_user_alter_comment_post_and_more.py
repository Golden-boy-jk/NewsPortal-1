# Generated by Django 5.1.4 on 2025-02-10 20:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="news.post",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="news.author",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                related_name="posts", through="news.PostCategory", to="news.category"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="type",
            field=models.CharField(
                choices=[("AR", "Статья"), ("NW", "Новость")],
                default="AR",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="postcategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category_posts",
                to="news.category",
            ),
        ),
        migrations.AlterField(
            model_name="postcategory",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_categories",
                to="news.post",
            ),
        ),
    ]
