# Generated by Django 3.1.3 on 2020-12-10 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201210_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='large_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='medium_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='small_stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
