# Generated by Django 5.1.3 on 2024-12-15 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_discuss', '0010_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
