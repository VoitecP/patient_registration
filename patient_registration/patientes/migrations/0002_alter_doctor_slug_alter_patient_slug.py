# Generated by Django 4.0 on 2023-01-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
