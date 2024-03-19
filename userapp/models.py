from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    confrimpassword = models.CharField(max_length=255)

    class Meta:
        db_table = "signupdetailstable"

class ContactModel(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    comment = models.TextField(max_length=255)
    email = models.EmailField(blank=False)

    class Meta:
        db_table = "contactus"
