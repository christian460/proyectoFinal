# Generated by Django 2.1.5 on 2020-07-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='sexo',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], default='M', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]