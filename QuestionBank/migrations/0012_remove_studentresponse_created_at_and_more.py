# Generated by Django 5.0.6 on 2024-06-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionBank', '0011_studentresponse_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresponse',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='studentresponse',
            name='updated_at',
        ),
    ]
