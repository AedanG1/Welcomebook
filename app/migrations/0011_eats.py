# Generated by Django 5.0.7 on 2024-08-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_information_options_information_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eats',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('drive_distance', models.IntegerField()),
                ('text', models.CharField(max_length=300)),
                ('website', models.CharField(blank=True, max_length=300)),
                ('phone', models.IntegerField()),
                ('position', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
