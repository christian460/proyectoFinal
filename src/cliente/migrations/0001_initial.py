# Generated by Django 2.1.5 on 2020-07-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
