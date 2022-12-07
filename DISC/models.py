from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Card(models.Model):
    dominante = models.CharField(max_length=200)
    influyente = models.CharField(max_length=200)
    estable = models.CharField(max_length=200)
    conciensudo = models.CharField(max_length=200)
    orden = models.CharField(max_length=4, default="1234")
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


"""
class Attribute(models.Model):
    attribute = models.CharField(max_length=200)
    value = models.CharField(max_length=1)

    def __str__(self):
        return str(self.attribute)



class Feature(models.Model):
    feature = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    attribute = models.ForeignKey(Attribute)

    def __str__(self):
        return str(self.feature)
"""


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    profile = models.CharField(max_length=200)
    emocion = models.CharField(max_length=200)
    juicio = models.CharField(max_length=200)
    influencia = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    abuso = models.CharField(max_length=200)
    presion = models.CharField(max_length=200)
    temor = models.CharField(max_length=200)
    eficacia = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.profile


class Segment(models.Model):
    id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Answer(models.Model):
    positive = models.CharField(max_length=200)
    negative = models.CharField(max_length=200)
    DISC = models.IntegerField(default=0)
    D = models.IntegerField(default=0)
    I = models.IntegerField(default=0)
    S = models.IntegerField(default=0)
    C = models.IntegerField(default=0)
    ans_date = models.DateTimeField('date published')

    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.segment_id
