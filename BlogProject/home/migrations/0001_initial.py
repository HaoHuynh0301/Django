# Generated by Django 3.2 on 2021-04-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=3000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]