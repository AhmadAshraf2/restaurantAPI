# Generated by Django 2.0.4 on 2018-04-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('opens_at', models.TimeField()),
                ('closes_at', models.TimeField()),
            ],
        ),
    ]