# Generated by Django 3.2.7 on 2021-10-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
