# Generated by Django 3.2.6 on 2023-03-31 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(blank=True, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=11, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('bank_type', models.CharField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Black', 'Black')], default='Gold', max_length=100)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
