# Generated by Django 5.0.6 on 2024-08-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_money_ngo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='ngo_id',
            field=models.IntegerField(null=True),
        ),
    ]
