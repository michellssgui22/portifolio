# Generated by Django 4.1.4 on 2022-12-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoapresentacao',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]