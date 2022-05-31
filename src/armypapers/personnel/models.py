from django.db import models

class Order(models.Model):
    number = models.CharField(max_length=5)
    date = models.DateField('order date')

class Warrior(models.Model):
    family_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    birth_date = models.DateField('date of birth', null=True, blank=True)
    id_number = models.CharField(max_length=10)
    passport = models.CharField(max_length=200)
    military_rank = models.CharField(max_length=50)
    military_idcard = models.CharField(max_length=200)
    military_commissariat = models.CharField(max_length=200)
    warfare_participant = models.CharField(max_length=200)
    scribe_address = models.CharField(max_length=200)
    residence_address = models.CharField(max_length=200)
    #relatives
    education_type = models.CharField(max_length=20)
    education_institution = models.CharField(max_length=200)
    education_year = models.CharField(max_length=4)
    education_speciality = models.CharField(max_length=200)
    weapon_type = models.CharField(max_length=50)
    weapon_number = models.CharField(max_length=50)
    bank_card = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)

    list_number = models.IntegerField(default=0)
    military_orders = models.ManyToManyField(Order)
    military_state = models.CharField(max_length=200, default='') # посада
    ato_oos_state = models.CharField(max_length=200, default='')
    resign_date = models.DateField('resigned to service date', null=True, blank=True)
    resign_division = models.CharField(max_length=200, default='') # Яким ТЦК прийнятий

    family_state = models.CharField(max_length=50, default='')
    

class Relative(models.Model):
    warrior = models.ForeignKey(Warrior, on_delete=models.CASCADE)
    relation = models.CharField(max_length=20)
    full_name = models.CharField(max_length=200)
    residence_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
