# Generated by Django 5.0.6 on 2024-06-11 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionBank', '0007_generated_questions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_questions', models.TextField()),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionBank.evaluatorai')),
            ],
        ),
    ]
