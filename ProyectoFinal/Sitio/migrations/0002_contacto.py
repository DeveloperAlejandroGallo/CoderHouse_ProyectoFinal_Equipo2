# Generated by Django 4.1.3 on 2022-11-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(default='', max_length=40)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]