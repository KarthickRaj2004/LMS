# Generated by Django 5.0.2 on 2024-02-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover_photo', models.ImageField(default='default_cover.jpg', upload_to='covers/')),
            ],
        ),
    ]
