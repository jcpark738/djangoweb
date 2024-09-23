# Generated by Django 3.2.24 on 2024-09-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('subtext', models.TextField()),
                ('schedule', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
