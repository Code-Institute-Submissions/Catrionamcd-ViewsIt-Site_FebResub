# Generated by Django 3.2.8 on 2021-10-25 19:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewsit_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug_url', models.SlugField(max_length=200, unique=True)),
                ('channel_post', models.CharField(max_length=200)),
                ('post_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('post_url', models.URLField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorposts', to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channelposts', to='viewsit_app.channel')),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
