# Generated by Django 2.2 on 2021-09-05 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0005_auto_20210904_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(related_name='books_liked', to='books_app.User'),
        ),
    ]
