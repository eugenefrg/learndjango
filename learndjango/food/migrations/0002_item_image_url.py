# Generated by Django 4.2.4 on 2023-09-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.CharField(default='https://placehold.co/600x400', max_length=500),
        ),
    ]
