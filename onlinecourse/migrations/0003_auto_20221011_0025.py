# Generated by Django 3.1.3 on 2022-10-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221011_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.IntegerField(),
        ),
    ]
