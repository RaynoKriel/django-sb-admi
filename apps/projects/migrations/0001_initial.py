# Generated by Django 3.2.6 on 2021-10-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.TextField()),
                ('description', models.TextField()),
                ('created', models.TextField()),
                ('modified', models.TextField()),
                ('user', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
    ]