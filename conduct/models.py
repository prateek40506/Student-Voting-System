from django.db import models

# Create your models here.


class Contestant(models.Model):
    gender_options = (
        ('male', 'male'),
        ('female', 'female')
    )
    position_choices = (
        ('Head Boy', 'Head Boy'),
        ('Head Girl', 'Head Girl'),
        ('Vice Head Boy', 'Vice Head Boy'),
        ('Vice Head Girl', 'Vice Head Girl'),
        ('Sports Captain', 'Sports Captain'),
        ('Vice Sports Captain', 'Vice Sports Captain')
    )
    contestant_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=gender_options, default='male')
    position = models.CharField(max_length=100, choices=position_choices, default='Head Boy')
    votes = models.IntegerField()

    def __str__(self):
        return self.contestant_name


class Account(models.Model):
    class_choices = (
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    section_choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
    )

    contestant = models.ManyToManyField(Contestant, blank=True)
    first_name = models.CharField(max_length=100, default='Prateek')
    last_name = models.CharField(max_length=100, default='Jain')
    voter_class = models.CharField(max_length=10, choices=class_choices, default='6')
    voter_section = models.CharField(max_length=10, choices=section_choices, default='A')

    def __str__(self):
        return self.first_name + " " + self.last_name



