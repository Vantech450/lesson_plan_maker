# Generated by Django 5.0.2 on 2024-02-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_pdf_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_files',
            name='pdfFiles',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]
