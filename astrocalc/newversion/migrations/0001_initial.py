# Generated by Django 4.1.4 on 2022-12-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Key')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('street', models.CharField(max_length=200, verbose_name='Street')),
                ('house', models.CharField(max_length=50, verbose_name='House')),
            ],
        ),
    ]
