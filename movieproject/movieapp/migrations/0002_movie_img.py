# Generated by Django 4.0.2 on 2022-03-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='gdhgdh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
