# Generated by Django 2.2.4 on 2019-10-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0006_video_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumb',
            field=models.ImageField(upload_to='thumb'),
        ),
    ]
