# Generated by Django 4.1.3 on 2022-11-22 02:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import movie.submodels.actor
import movie.submodels.poster
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1, verbose_name='Status')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='Published Date')),
                ('imdb_rating', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='IMDB Rating')),
                ('budget', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Movie Budget')),
                ('trailer', models.FileField(blank=True, null=True, upload_to='', verbose_name='Trailer')),
                ('thumbnail', models.ImageField(null=True, upload_to='movie/images/', verbose_name='Thumbnail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=movie.submodels.poster.poster_directory_path, verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movie.movie')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Fullname')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(null=True, verbose_name='Text')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='Slug')),
                ('city', models.CharField(max_length=16, verbose_name="User's City")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='By User')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.movie')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='movie.review', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='Is Valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='movie.movie')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, null=True, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=32, null=True, verbose_name='Lastname')),
                ('role', models.CharField(choices=[('A', 'Actor'), ('D', 'Director')], max_length=1, null=True, verbose_name='Role')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('avatar', models.ImageField(null=True, upload_to=movie.submodels.actor.actor_avatar_directory_path, verbose_name='Avatar')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='movie.movie')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
                'ordering': ('-first_name',),
            },
        ),
    ]
