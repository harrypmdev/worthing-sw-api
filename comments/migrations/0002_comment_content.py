# Generated by Django 4.2 on 2025-03-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
