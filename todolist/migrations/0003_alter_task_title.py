# Generated by Django 3.2.4 on 2021-06-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20210630_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=350),
        ),
    ]