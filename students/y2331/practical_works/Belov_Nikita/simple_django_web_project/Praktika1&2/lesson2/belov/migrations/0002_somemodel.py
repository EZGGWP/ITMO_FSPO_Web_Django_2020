# Generated by Django 3.0.3 on 2020-05-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('descript', models.TextField()),
            ],
        ),
    ]
