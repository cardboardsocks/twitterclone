# Generated by Django 3.1.1 on 2020-09-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20200908_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='mentioned_user',
            new_name='user_notification',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_active',
        ),
        migrations.AddField(
            model_name='notification',
            name='viewed_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
