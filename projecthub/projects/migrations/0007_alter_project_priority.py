# Generated by Django 5.2.3 on 2025-06-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default='M', max_length=1),
        ),
    ]
