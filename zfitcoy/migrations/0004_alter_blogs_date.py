# Generated by Django 4.0.2 on 2022-05-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zfitcoy', '0003_air_image_body_typess_image_earth_image_fire_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
