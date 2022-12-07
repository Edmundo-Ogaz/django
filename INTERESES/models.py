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


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Variant(models.Model):
    id = models.IntegerField(primary_key=True)
    variant = models.CharField(max_length=25)
    question = models.CharField(max_length=200)
    conclusion = models.CharField(max_length=200)

    def __str__(self):
        return self.variant


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    attributes = models.ManyToManyField(Variant)
    image_url = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.attribute


class Option(models.Model):
    description = models.CharField(max_length=200)
    attribute = models.ForeignKey(Attribute, default=None, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Percentage(models.Model):
    attribute = models.ForeignKey(Attribute, default=None, null=True, on_delete=models.CASCADE)
    sum = models.IntegerField()
    percentage = models.IntegerField()

    def __str__(self):
        return str(self.percentage)


class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(Percentage)

    def __str__(self):
        return "ANSWER_OBJECT"



