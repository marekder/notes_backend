# Generated by Django 4.2 on 2023-04-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_alter_document_options_alter_document_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
