# Generated by Django 4.2 on 2023-04-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={},
        ),
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
