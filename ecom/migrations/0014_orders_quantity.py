# Generated by Django 3.0.5 on 2023-06-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0013_auto_20230617_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
