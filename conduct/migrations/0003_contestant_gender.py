# Generated by Django 4.0.6 on 2022-07-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conduct', '0002_contestant_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100),
        ),
    ]