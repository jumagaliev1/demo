# Generated by Django 4.0.1 on 2022-04-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0005_feedbackitemmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackitemmodel',
            name='item',
            field=models.IntegerField(default=-1),
        ),
    ]