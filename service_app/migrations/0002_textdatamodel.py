# Generated by Django 2.2.18 on 2022-06-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_text', models.TextField()),
                ('created_file', models.FileField(upload_to='')),
            ],
        ),
    ]
