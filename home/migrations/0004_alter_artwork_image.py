# Generated by Django 3.2.3 on 2021-05-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_artwork_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
