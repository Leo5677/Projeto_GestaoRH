# Generated by Django 3.2.3 on 2021-05-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome Da Empresa'),
        ),
    ]
