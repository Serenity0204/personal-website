# Generated by Django 4.1.5 on 2023-01-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_created_alter_project_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]