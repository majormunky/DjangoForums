# Generated by Django 4.1.4 on 2023-01-03 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0002_forumpost_forum"),
    ]

    operations = [
        migrations.AddField(
            model_name="forumpost",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="forum.forumpost",
            ),
        ),
    ]
