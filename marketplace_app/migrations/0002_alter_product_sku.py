# Generated by Django 4.1.4 on 2022-12-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='SKU',
            field=models.CharField(default='310IQ33', editable=False, max_length=50, unique=True),
        ),
    ]
