# Generated by Django 3.0.6 on 2020-06-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20200607_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew_member',
            name='id_flight',
        ),
        migrations.AddField(
            model_name='flight_information',
            name='id_crew_member_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flight_information',
            name='id_crew_member_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flight_information',
            name='id_crew_member_3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
