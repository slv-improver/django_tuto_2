# Generated by Django 4.1.1 on 2022-10-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="word_count",
            field=models.IntegerField(null=True),
        ),
    ]
