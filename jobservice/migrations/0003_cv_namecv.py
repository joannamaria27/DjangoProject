# Generated by Django 2.2 on 2019-05-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobservice', '0002_auto_20190504_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='nameCv',
            field=models.CharField(default='', max_length=50),
        ),
    ]