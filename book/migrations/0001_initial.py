# Generated by Django 3.0.7 on 2020-06-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=32, unique=True)),
                ('book_author', models.CharField(max_length=32)),
                ('book_type', models.CharField(max_length=32)),
                ('book_price', models.CharField(max_length=32)),
                ('book_press', models.CharField(max_length=32)),
            ],
        ),
    ]