# Generated by Django 4.2.5 on 2023-09-16 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicinal_Use",
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
                ("health_issue", models.CharField(max_length=250)),
                ("dosage_and_formulation", models.CharField(max_length=250)),
                ("part_used", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Plant",
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
                ("local_name", models.CharField(max_length=250)),
                ("english_name", models.CharField(max_length=250)),
                ("scientific_name", models.CharField(max_length=250)),
                ("description", models.CharField(max_length=250)),
                ("areas_in_Uganda", models.CharField(max_length=250)),
                ("life_form", models.CharField(max_length=250)),
                ("climate_impact", models.CharField(max_length=250)),
                ("economic_value", models.CharField(max_length=250)),
                ("notes", models.CharField(max_length=250)),
                ("images", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "videos",
                    models.FileField(blank=True, null=True, upload_to="media_files"),
                ),
                (
                    "audio",
                    models.FileField(blank=True, null=True, upload_to="media_files"),
                ),
                ("citation", models.CharField(max_length=250)),
                ("date_entered", models.DateTimeField(auto_now_add=True)),
                (
                    "contributor_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "medicinal_use",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="plants_app.medicinal_use",
                    ),
                ),
            ],
            options={
                "ordering": ["local_name"],
            },
        ),
    ]
