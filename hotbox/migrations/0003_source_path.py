# Generated by Django 3.2.9 on 2021-11-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotbox', '0002_auto_20211106_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='path',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
