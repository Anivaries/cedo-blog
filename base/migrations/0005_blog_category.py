# Generated by Django 4.2.2 on 2023-06-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_blog_game_name_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('R', 'Review'), ('N', 'News'), ('O', 'Opinion'), ('H', 'Hardware')], max_length=10),
        ),
    ]
