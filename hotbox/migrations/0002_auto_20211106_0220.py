# Generated by Django 3.2.9 on 2021-11-06 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='host',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='source',
            name='password',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='source',
            name='port',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='source',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]