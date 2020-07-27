# Generated by Django 2.1.5 on 2020-07-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0003_ropa_prom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa',
            old_name='color',
            new_name='cat',
        ),
        migrations.RemoveField(
            model_name='ropa',
            name='material',
        ),
        migrations.RemoveField(
            model_name='ropa',
            name='talla',
        ),
        migrations.AddField(
            model_name='ropa',
            name='des',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
