# Generated by Django 3.2.16 on 2023-06-08 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256, verbose_name="Заголовок")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "slug",
                    models.SlugField(
                        max_length=64, unique=True, verbose_name="Идентификатор"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Добавлено"),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=256, verbose_name="Название места"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Добавлено"),
                ),
            ],
            options={
                "verbose_name": "местоположение",
                "verbose_name_plural": "Местоположения",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время публикации"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                ("created_at", models.DateTimeField(verbose_name="Добавлено")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор публикации",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="posts",
                        to="blog.category",
                        verbose_name="категория",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="location",
                        to="blog.location",
                        verbose_name="местоположение",
                    ),
                ),
            ],
            options={
                "verbose_name": "публикация",
                "verbose_name_plural": "Публикации",
            },
        ),
    ]
