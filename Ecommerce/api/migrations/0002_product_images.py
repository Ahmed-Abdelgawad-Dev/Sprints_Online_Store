# Generated by Django 4.0.4 on 2022-06-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
