# Generated by Django 5.0.6 on 2024-05-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='mesa',
            field=models.TextField(),
        ),
    ]
