# Generated by Django 5.2.1 on 2025-05-29 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_recenzent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SzablonZdarzenia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255)),
                ('opis', models.TextField(blank=True, null=True)),
                ('czy_aktywny', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_zdarzenia', models.DateField()),
                ('opis', models.TextField(blank=True, null=True)),
                ('utworzono_przez', models.CharField(max_length=255)),
                ('doktorat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doktorat')),
                ('szablon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.szablonzdarzenia')),
            ],
        ),
    ]
