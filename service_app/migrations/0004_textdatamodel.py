# Generated by Django 2.2.18 on 2022-06-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0003_delete_textdatamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_text', models.TextField()),
                ('transcrib', models.FileField(upload_to='')),
            ],
        ),
    ]
