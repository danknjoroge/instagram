# Generated by Django 4.0.3 on 2022-04-01 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_alter_image_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img_caption',
            new_name='image_caption',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='img_name',
            new_name='image_name',
        ),
    ]
