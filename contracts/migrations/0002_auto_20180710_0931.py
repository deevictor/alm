# Generated by Django 2.0.7 on 2018-07-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_start',
            field=models.DateField(),
        ),
    ]