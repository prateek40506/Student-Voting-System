# Generated by Django 4.0.6 on 2022-08-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conduct', '0008_alter_account_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='position',
            field=models.CharField(choices=[('Head Boy', 'Head Boy'), ('Head Girl', 'Head Girl'), ('Vice Head Boy', 'Vice Head Boy'), ('Vice Head Girl', 'Vice Head Girl'), ('Sports Captain', 'Sports Captain'), ('Vice Sports Captain', 'Vice Sports Captain')], default='Head Boy', max_length=100),
        ),
    ]
