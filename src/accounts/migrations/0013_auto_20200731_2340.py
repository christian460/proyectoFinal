# Generated by Django 2.1.5 on 2020-07-31 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200731_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], max_length=100),
        ),
    ]