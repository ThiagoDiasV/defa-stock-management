# Generated by Django 3.0.3 on 2020-04-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('withdrawal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='withdrawal',
            options={'ordering': ['date']},
        ),
    ]
