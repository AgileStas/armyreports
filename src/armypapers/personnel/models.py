from django.db import models

class Order(models.Model):
    number = models.CharField(max_length=5)
    date = models.DateField('order date')
    issuer = models.CharField(max_length=50, default='')

class Division(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=25)
    full_name = models.CharField(max_length=250)
    full_name_form1 = models.CharField(max_length=250) # full name in form that should be used for full position name
    semifull_name = models.CharField(max_length=250)
    semifull_name_form1 = models.CharField(max_length=250) # semifull name in form that should be used for full position name

class Rank(models.Model):
    RANKTYPE_CHOICES = (
        ('1', 'Солдат'),
        ('2', 'Сержант'),
        ('3', 'Офіцер'),
    )
    name = models.CharField(max_length=20)
    rtype = models.CharField(max_length=1, choices=RANKTYPE_CHOICES)
    code = models.CharField(max_length=15, default='')
    name_f1 = models.CharField(max_length=20, default='')
    name_f2 = models.CharField(max_length=20, default='')
    short_name = models.CharField(max_length=15, default='')
    short_name_f1 = models.CharField(max_length=15, default='')
    short_name_f2 = models.CharField(max_length=15, default='')
    shortest_name = models.CharField(max_length=10, default='')
    shortest_name_f1 = models.CharField(max_length=10, default='')
    shortest_name_f2 = models.CharField(max_length=10, default='')

class RankOrder(models.Model):
    warrior = models.ForeignKey('Warrior', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    current = models.BooleanField()

class StateChange(models.Model):
    STATETYPE_CHOICES = ( # Тип зміни стану відношення до вій
        ('1', 'Призваний'),
        ('2', 'Зміна посади/частини'),
        ('3', 'Звільнений'),
    )
    warrior = models.ForeignKey('Warrior', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    change_type = models.CharField(max_length=1, choices=STATETYPE_CHOICES)
    change_date = models.DateField('state change date', null=True, blank=True)
    change_comment = models.CharField(max_length=50, default='')
    mu_name = models.CharField(max_length=25) # Назва військової частини -- Military Unit Name
    mu_comment = models.CharField(max_length=50, default='') # Коментар до назви військової частини

class Position(models.Model):
    list_number = models.IntegerField(default=0)
    name = models.CharField(max_length=15)
    #full_name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    tarif = models.IntegerField(default=0)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, null=True, blank=True)
    classificator = models.CharField(max_length=15, default='')

    @property
    def full_name(self):
        return self.name + ' ' + self.division.full_name_form1

    @property
    def semifull_name(self):
        return self.name + ' ' + self.division.semifull_name_form1

class Weapon(models.Model):
    wtype = models.CharField(max_length=50, default='') # Пістолет, автомат, кулемет
    wmodel = models.CharField(max_length=50, default='') # ПМ, АК-74, ...
    ammo_caliber = models.CharField(max_length=10, default='')

class IdDocument(models.Model):
    # 'Паспорт', 'Військовий квиток', 'УБД'
    d_type = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    issue_date = models.DateField('issue date', null=True, blank=True)
    issue_org = models.CharField(max_length=100, default='')

class ContactPerson(models.Model):
    family_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    birth_date = models.DateField('date of birth', null=True, blank=True)
    scribe_address = models.CharField(max_length=200)
    residence_address = models.CharField(max_length=200)

    @property
    def initials(self):
        fa = self.first_name.split()
        return fa[0][0] + '.' + fa[1][0] + '.'

    @property
    def full_name(self):
        return self.family_name + ' ' + self.first_name

    @property
    def full_name_initials(self):
        return self.family_name + ' ' + self.initials

class PersonRelation(models.Model): # person1 is person2 relation
    person1 = models.ForeignKey(ContactPerson, related_name='person1', on_delete=models.CASCADE)
    relation = models.CharField(max_length=20)
    person2 = models.ForeignKey(ContactPerson, related_name='person2', on_delete=models.CASCADE)

class Warrior(models.Model):
    person = models.OneToOneField(ContactPerson, on_delete=models.CASCADE, null=True, blank=True)
    wid_passport = models.OneToOneField(IdDocument, related_name='passport', on_delete=models.CASCADE, null=True, blank=True)
    wid_military = models.OneToOneField(IdDocument, related_name='military_idcard', on_delete=models.CASCADE, null=True, blank=True)
    wid_warfare = models.OneToOneField(IdDocument, related_name='warfare_idcard', on_delete=models.CASCADE, null=True, blank=True)
    id_number = models.CharField(max_length=10)

    education_type = models.CharField(max_length=20)
    education_institution = models.CharField(max_length=200)
    education_year = models.CharField(max_length=4)
    education_speciality = models.CharField(max_length=200)

    bank_card = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)

    military_commissariat = models.CharField(max_length=200)

    military_orders = models.ManyToManyField(Order)

    position = models.OneToOneField(Position, related_name='position', on_delete=models.CASCADE, null=True, blank=True)
    position_fact = models.OneToOneField(Position, related_name='position_fact', on_delete=models.CASCADE, null=True, blank=True)

    ato_oos_state = models.CharField(max_length=200, default='')
    resign_date = models.DateField('resigned to service date', null=True, blank=True)
    resign_division = models.CharField(max_length=200, default='') # Яким ТЦК прийнятий

    family_state = models.CharField(max_length=50, default='')
    
    blood_group = models.CharField(max_length=10, default='')

    call_sign = models.CharField(max_length=50, default='')
    
    foot_size = models.CharField(max_length=10, default='')
    head_size = models.CharField(max_length=10, default='')
    wear_size = models.CharField(max_length=10, default='')

    @property
    def m_rank(self):
        #ro = RankOrder.objects.filter(warrior_id=self.id).filter(current=True)
        #RankOrder.objects.get(id=94)
        #print('--------- ' + ro[0].warrior.military_rank)
        #print('========= ' + ro[0].rank.name)
        #return ro[0].rank
        return RankOrder.objects.get(warrior_id=self.id, current=True).rank

    @property
    def rank_orders(self):
        return RankOrder.objects.filter(warrior_id=self.id)

    @property
    def weapons(self):
        #return WarriorWeapon.objects.select_related.all()
        return WarriorWeapon.objects.filter(warrior_id=self.id)

    @property
    def relations(self):
        #return PersonRelation.objects.select_related.all()
        return PersonRelation.objects.filter(person1_id=self.person.id)

    @property
    def state_changes(self):
        #return StateChange.objects.select_related.all()
        return StateChange.objects.filter(warrior_id=self.id)

class WarriorWeapon(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    wnumber = models.CharField(max_length=50, default='')
    wyear = models.CharField(max_length=5, default='')
    ammo_amount = models.IntegerField(default=0)
    warrior = models.ForeignKey(Warrior, on_delete=models.CASCADE)
    w_doc = models.ForeignKey(IdDocument, on_delete=models.CASCADE, null=True, blank=True)
