# Generated by Django 2.2.4 on 2019-10-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20191008_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
