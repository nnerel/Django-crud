# Generated by Django 3.2.6 on 2021-08-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210821_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
