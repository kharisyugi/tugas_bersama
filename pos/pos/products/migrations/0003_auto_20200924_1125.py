# Generated by Django 2.2 on 2020-09-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200924_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cate',
            name='name_c',
            field=models.CharField(default='', max_length=30),
        ),
    ]
