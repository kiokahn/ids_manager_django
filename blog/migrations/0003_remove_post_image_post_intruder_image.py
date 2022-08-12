# Generated by Django 4.0.3 on 2022-06-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='intruder_image',
            field=models.ImageField(default='intruder_image/default_error.png', upload_to='intruder_image/%Y/%m/%d/'),
        ),
    ]