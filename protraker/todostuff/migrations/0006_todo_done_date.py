# Generated by Django 3.1.6 on 2021-03-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todostuff', '0005_todo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done_date',
            field=models.DateField(auto_now=True),
        ),
    ]
