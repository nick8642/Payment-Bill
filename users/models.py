from django.db import models


# Create your models here.

class Branch_Master(models.Model):
    name = models.TextField(max_length=45)
    address = models.TextField(max_length=100)
    city = models.TextField(max_length=50)
    phone = models.TextField(max_length=11)


class Course_Master(models.Model):
    name = models.TextField(max_length=50)
    fees = models.FloatField()
    bid = models.IntegerField()
    seats = models.IntegerField()


class Account_Master(models.Model):
    name = models.TextField(max_length=100)
    uname = models.TextField(max_length=100)
    pwd = models.TextField()
    mno = models.TextField(max_length=10)
    address = models.TextField()
    bid = models.IntegerField()
    doj = models.TextField(max_length=15)
    salary = models.FloatField()
    email = models.TextField(max_length=100)
    branch = models.TextField()


class Student_Master(models.Model):
    name = models.TextField(max_length=20)
    email = models.TextField(max_length=30)
    mno = models.TextField(max_length=10)
    cid = models.IntegerField()
    bid = models.IntegerField()
    address = models.TextField()
    doj = models.TextField()
    paid = models.FloatField()
    balance = models.FloatField()
    course = models.TextField()
