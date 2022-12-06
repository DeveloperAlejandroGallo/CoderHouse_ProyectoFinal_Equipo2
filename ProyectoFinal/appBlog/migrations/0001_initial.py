# Generated by Django 4.1.3 on 2022-11-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=40)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=40)),
                ('apellido', models.CharField(default='', max_length=40)),
                ('edad', models.IntegerField(default=0)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=50)),
                ('fecha', models.DateField()),
                ('texto', models.CharField(default='', max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=40)),
                ('apellido', models.CharField(default='', max_length=40)),
                ('edad', models.IntegerField(default=0)),
                ('profesion', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]