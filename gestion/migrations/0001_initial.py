# Generated by Django 4.2.14 on 2024-07-30 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Copropriete",
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
                ("nom", models.CharField(max_length=200)),
                ("adresse", models.CharField(max_length=300)),
                ("nombre_lots", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Travaux",
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
                ("description", models.TextField()),
                ("date_debut", models.DateField()),
                ("date_fin", models.DateField(blank=True, null=True)),
                ("cout", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sinistre",
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
                ("description", models.TextField()),
                ("date_sinistre", models.DateField()),
                ("date_resolution", models.DateField(blank=True, null=True)),
                (
                    "cout",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coproprietaire",
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
                ("nom", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("telephone", models.CharField(max_length=20)),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContratMaintenance",
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
                ("fournisseur", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("date_debut", models.DateField()),
                ("date_fin", models.DateField(blank=True, null=True)),
                ("cout_annuel", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BudgetPrevisionnel",
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
                ("annee", models.IntegerField()),
                ("montant_prevu", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "montant_reel",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssembleeGenerale",
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
                ("date", models.DateField()),
                ("ordre_du_jour", models.TextField()),
                ("proces_verbal", models.TextField(blank=True, null=True)),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AppelFonds",
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
                ("date_appel", models.DateField()),
                ("montant", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_limite", models.DateField()),
                (
                    "copropriete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.copropriete",
                    ),
                ),
            ],
        ),
    ]
