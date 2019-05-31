# Generated by Django 2.2 on 2019-05-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cidade',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='codigo',
            field=models.IntegerField(null=True, verbose_name=8),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.IntegerField(null=True, verbose_name=4),
        ),
        migrations.AddField(
            model_name='usuario',
            name='datanasc',
            field=models.IntegerField(null=True, verbose_name=4),
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero',
            field=models.IntegerField(null=True, verbose_name=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rg',
            field=models.IntegerField(null=True, verbose_name=10),
        ),
    ]
