# Generated by Django 3.1.2 on 2020-11-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0008_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/imageuploads/'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/imageuploads/'),
        ),
    ]
