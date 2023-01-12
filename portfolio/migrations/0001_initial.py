# Generated by Django 4.1.5 on 2023-01-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('github_link', models.CharField(max_length=500)),
                ('tech_stack', models.TextField()),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]