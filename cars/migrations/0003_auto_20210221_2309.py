# Generated by Django 3.1.7 on 2021-02-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210221_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Вин'),
        ),
    ]