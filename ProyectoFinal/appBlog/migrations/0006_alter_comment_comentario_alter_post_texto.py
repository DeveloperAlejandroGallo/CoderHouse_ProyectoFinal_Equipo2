# Generated by Django 4.1.2 on 2022-12-10 02:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0005_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comentario',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]