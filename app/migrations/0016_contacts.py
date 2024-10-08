# Generated by Django 5.0.7 on 2024-08-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_activities_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('address_one', models.CharField(max_length=300)),
                ('address_two', models.CharField(max_length=300)),
                ('position', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
