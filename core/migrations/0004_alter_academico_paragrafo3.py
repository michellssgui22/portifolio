# Generated by Django 4.1.4 on 2022-12-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_academico_alter_projetos_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academico',
            name='paragrafo3',
            field=models.TextField(default='', max_length=1000, verbose_name='Terceiro Praragrafo'),
        ),
    ]
