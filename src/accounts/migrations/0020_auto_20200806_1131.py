# Generated by Django 2.1.5 on 2020-08-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=100),
        ),
    ]
