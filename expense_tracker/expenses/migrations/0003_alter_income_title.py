# Generated by Django 5.1.2 on 2024-10-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_income_alter_expense_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
