# Generated by Django 5.0.6 on 2024-06-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uername', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
                ('high_score', models.IntegerField()),
            ],
        ),
    ]