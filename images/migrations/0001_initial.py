# Generated by Django 3.2.3 on 2021-05-20 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_image', models.CharField(blank=True, max_length=255, null=True)),
                ('image_format', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TagsImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_img', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tags_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tagsimg_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'tagsimg_images',
                'managed': False,
            },
        ),
    ]
