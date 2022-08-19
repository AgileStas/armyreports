from django.db import models

class Order(models.Model):
    number = models.CharField(max_length=5)
    date = models.DateField('order date')

class Weapon(models.Model):
    wtype = models.CharField(max_length=50, default='') # Пістолет, автомат, кулемет
    wmodel = models.CharField(max_length=50, default='') # ПМ, АК-74, ...
    ammo_caliber = models.CharField(max_length=10, default='')

class Warrior(models.Model):
    family_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    birth_date = models.DateField('date of birth', null=True, blank=True)
    id_number = models.CharField(max_length=10)
    passport = models.CharField(max_length=200)
    military_rank = models.CharField(max_length=50)
    military_idcard = models.CharField(max_length=200, default='')
    military_iddate = models.DateField('military idcard issue date', null=True, blank=True)
    military_idissued = models.CharField(max_length=200, default='')
    military_commissariat = models.CharField(max_length=200)
    warfare_participant = models.CharField(max_length=200)
    scribe_address = models.CharField(max_length=200)
    residence_address = models.CharField(max_length=200)
    #relatives
    education_type = models.CharField(max_length=20)
    education_institution = models.CharField(max_length=200)
    education_year = models.CharField(max_length=4)
    education_speciality = models.CharField(max_length=200)

    bank_card = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)

    list_number = models.IntegerField(default=0)
    military_orders = models.ManyToManyField(Order)
    military_state = models.CharField(max_length=200, default='') # посада
    ato_oos_state = models.CharField(max_length=200, default='')
    resign_date = models.DateField('resigned to service date', null=True, blank=True)
    resign_division = models.CharField(max_length=200, default='') # Яким ТЦК прийнятий

    family_state = models.CharField(max_length=50, default='')
    
    blood_group = models.CharField(max_length=10, default='')

    call_sign = models.CharField(max_length=50, default='')
    
    foot_size = models.CharField(max_length=10, default='')
    head_size = models.CharField(max_length=10, default='')
    wear_size = models.CharField(max_length=10, default='')

class WarriorWeapon(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    wnumber = models.CharField(max_length=50, default='')
    wyear = models.CharField(max_length=5, default='')
    ammo_amount = models.IntegerField(default=0)
    doctype = models.CharField(max_length=50, default='')
    document = models.CharField(max_length=50, default='')
    warrior = models.ForeignKey(Warrior, on_delete=models.CASCADE)

class Relative(models.Model):
    warrior = models.ForeignKey(Warrior, on_delete=models.CASCADE)
    relation = models.CharField(max_length=20)
    full_name = models.CharField(max_length=200)
    residence_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
