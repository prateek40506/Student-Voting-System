# Generated by Django 4.0.6 on 2022-07-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conduct', '0005_alter_account_contestant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='contestant',
        ),
        migrations.AddField(
            model_name='account',
            name='contestant',
            field=models.ManyToManyField(blank=True, to='conduct.contestant'),
        ),
    ]
