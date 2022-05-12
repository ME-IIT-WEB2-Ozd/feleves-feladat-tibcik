from django.db import models

# Create your models here.

class Patient(models.Model):
    FERFI = 'f'
    NO = 'n'

    CHOICE_NEM = {
        (FERFI, "Férfi"),
        (NO, "Nő"),
    }

    name = models.CharField(max_length=255)
    szul_date = models.DateField()
    taj = models.CharField(max_length=255)
    nem = models.CharField(max_length=10, choices=CHOICE_NEM)

class Treatment(models.Model):
    patient = models.ForeignKey(Patient, related_name='treatments', on_delete=models.CASCADE)
    kezeles = models.TextField()
    ido = models.DateTimeField(auto_now_add=True)

class Medicine(models.Model):
    treatment = models.ForeignKey(Treatment, related_name='medicines', on_delete=models.CASCADE)
    gyogyszer = models.CharField(max_length=255)

class Test(models.Model):
    FERFI = 'f'
    NO = 'n'
    MIND = 'm'

    CHOICE_NEM = {
        (FERFI, "Férfi"),
        (NO, "Nő"),
        (MIND, 'Mind')
    }

    name = models.CharField(max_length=255)
    nem = models.CharField(max_length=10, choices=CHOICE_NEM)
    kor = models.IntegerField()
    interval = models.IntegerField()

class Tested(models.Model):
    patient = models.ForeignKey(Patient, related_name='patients', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='tests', on_delete=models.CASCADE)
    utolso = models.DateTimeField(auto_now=True)
