# Generated by Django 5.0.2 on 2024-03-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
