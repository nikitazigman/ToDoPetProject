# Generated by Django 3.2.5 on 2021-07-16 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['-date']},
        ),
    ]
