# Generated by Django 5.1.5 on 2025-02-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcallnumber',
            name='library',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookcallnumber',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
