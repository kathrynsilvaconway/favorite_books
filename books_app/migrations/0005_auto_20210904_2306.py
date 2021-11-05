# Generated by Django 2.2 on 2021-09-05 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0004_auto_20210904_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(null=True, related_name='books_liked', to='books_app.User'),
        ),
        migrations.AlterField(
            model_name='book',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_uploaded', to='books_app.User'),
        ),
    ]
