# Generated by Django 4.0.6 on 2022-09-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
