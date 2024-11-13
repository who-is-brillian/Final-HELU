# Generated by Django 5.1.1 on 2024-11-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('start_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('sessions', models.IntegerField()),
                ('level', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
    ]
