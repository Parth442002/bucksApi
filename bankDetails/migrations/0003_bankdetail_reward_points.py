# Generated by Django 3.2.6 on 2023-03-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankDetails', '0002_bankcards'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetail',
            name='reward_points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
