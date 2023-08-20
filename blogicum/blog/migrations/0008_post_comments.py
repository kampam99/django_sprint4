# Generated by Django 3.2.16 on 2023-07-09 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_auto_20230709_1338"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="comments",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="blog.comment",
            ),
        ),
    ]
