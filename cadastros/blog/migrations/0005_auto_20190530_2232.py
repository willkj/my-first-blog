# Generated by Django 2.2 on 2019-05-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190530_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='datanasc',
            field=models.DateField(null=True),
        ),
    ]