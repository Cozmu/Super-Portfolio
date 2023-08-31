# Generated by Django 4.2.3 on 2023-08-31 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=500)),
                ("github_url", models.URLField()),
                ("keyword", models.CharField(max_length=50)),
                ("key_skill", models.CharField(max_length=50)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.profile",
                    ),
                ),
            ],
        ),
    ]
