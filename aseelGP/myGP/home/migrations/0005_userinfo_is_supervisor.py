# Generated by Django 4.2.7 on 2023-12-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_created_at_post_created_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_supervisor',
            field=models.BooleanField(default=False),
        ),
    ]
