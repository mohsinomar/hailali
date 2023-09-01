# Generated by Django 3.2.7 on 2022-06-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_admin', '0002_auto_20220615_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='berhil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarque', models.CharField(blank=True, max_length=100)),
                ('ouvriers', models.CharField(blank=True, max_length=100)),
                ('fonction', models.CharField(blank=True, max_length=100)),
                ('verger', models.CharField(blank=True, max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='hawara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarque', models.CharField(blank=True, max_length=100)),
                ('ouvriers', models.CharField(blank=True, max_length=100)),
                ('fonction', models.CharField(blank=True, max_length=100)),
                ('verger', models.CharField(blank=True, max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
