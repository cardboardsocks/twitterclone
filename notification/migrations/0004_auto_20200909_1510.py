# Generated by Django 3.1.1 on 2020-09-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20200909_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='viewed_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
