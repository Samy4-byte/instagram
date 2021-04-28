# Generated by Django 3.1 on 2021-04-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='postimage',
            old_name='product',
            new_name='post',
        ),
    ]
