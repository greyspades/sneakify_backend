# Generated by Django 4.0.4 on 2022-05-14 13:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0002_alter_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='item_cart',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, null=True, size=50),
        ),
    ]