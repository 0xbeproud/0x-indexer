# Generated by Django 5.0.1 on 2024-01-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=1024)),
                ('supply', models.IntegerField()),
                ('symbol', models.CharField(max_length=32)),
                ('discord_link', models.CharField(max_length=512)),
                ('twitter_link', models.CharField(max_length=512)),
                ('website_link', models.CharField(max_length=512)),
                ('imageURI', models.CharField(max_length=1024)),
            ],
        ),
    ]
