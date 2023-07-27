# Generated by Django 4.2.3 on 2023-07-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('contato', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('instituicao', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('trabalho', models.CharField(max_length=100)),
                ('observacoes', models.CharField(max_length=100)),
                ('data_inicio', models.DateField()),
                ('data_entrega', models.DateField()),
            ],
        ),
    ]