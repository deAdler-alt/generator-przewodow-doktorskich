# Generated by Django 5.2.1 on 2025-05-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=255)),
                ('nazwisko', models.CharField(max_length=255)),
                ('tytulStopien', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('stanowisko', models.CharField(max_length=255)),
                ('telefon', models.CharField(blank=True, max_length=20, null=True)),
                ('link_do_profilu_gov', models.URLField(blank=True, null=True)),
                ('specjalnosci', models.TextField(blank=True, null=True)),
                ('plec', models.CharField(max_length=1)),
                ('tytul_po', models.CharField(blank=True, max_length=255, null=True)),
                ('imie_nazwisko_dopelniacz', models.CharField(max_length=255)),
                ('imie_nazwisko_celownik', models.CharField(max_length=255)),
                ('imie_nazwisko_biernik', models.CharField(max_length=255)),
            ],
        ),
    ]
