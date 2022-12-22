# Generated by Django 4.1.4 on 2022-12-21 22:41

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_academico_paragrafo2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('curso', models.CharField(max_length=100, verbose_name='Título')),
                ('instituicao', models.TextField(verbose_name='Comentário')),
                ('urlvalidacao', models.URLField(verbose_name='URL GitHub')),
                ('totalHoras', models.URLField(verbose_name='URL Site')),
                ('dataConclusao', models.DateField(verbose_name='Data Conclusão')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': (450, 225)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
        ),
    ]