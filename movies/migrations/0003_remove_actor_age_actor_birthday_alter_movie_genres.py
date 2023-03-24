# Generated by Django 4.1.7 on 2023-03-24 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_world_premiere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='age',
        ),
        migrations.AddField(
            model_name='actor',
            name='birthday',
            field=models.DateField(default=datetime.date(2023, 3, 24), verbose_name='Дата Рождения'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre', verbose_name='Жанр'),
        ),
    ]