# Generated by Django 2.2.4 on 2019-09-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackhome', '0003_apartment_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='equipped',
            field=models.BooleanField(default=False),
        ),
    ]
