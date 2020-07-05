# Generated by Django 3.0.3 on 2020-06-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extendedusermodel',
            options={'permissions': [('add_voyage', 'You can add voyage')]},
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='b_day',
            field=models.DateField(default='1970-01-03'),
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='hire_date',
            field=models.DateField(default='1970-01-03'),
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='job_type',
            field=models.CharField(choices=[('CPT', 'captain'), ('SLR', 'sailor'), ('ACC', 'accountant')], default='sailor', max_length=20),
        ),
    ]