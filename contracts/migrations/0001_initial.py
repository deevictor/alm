# Generated by Django 2.0.7 on 2018-07-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=60)),
                ('contract_type', models.CharField(max_length=120)),
                ('currency_type', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('contract_value', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
