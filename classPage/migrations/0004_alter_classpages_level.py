# Generated by Django 5.1.3 on 2024-11-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classPage', '0003_alter_classpages_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classpages',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Standart', 'Standart'), ('Advanced', 'Advanced')], default='Beginner', max_length=50),
        ),
    ]
