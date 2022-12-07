from django.db import models

# Create your models here.

from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=200)
    guide = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Header(models.Model):
    header = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.header


class Row(models.Model):
    row = models.IntegerField(default=0)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.row)


class Cell(models.Model):
    content = models.CharField(max_length=200)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    header = models.ForeignKey(Header, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Instruction(models.Model):
    instruction = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.instruction


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    omitted = models.IntegerField(default=0)
    ans_date = models.DateTimeField('date published')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, default="Iniciado")

    def __str__(self):
        return self.score

