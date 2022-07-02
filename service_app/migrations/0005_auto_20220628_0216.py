# Generated by Django 2.2.18 on 2022-06-28 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0004_textdatamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textdatamodel',
            name='transcrib',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='textdatamodel',
            name='upload_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]