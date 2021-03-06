from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=18 , null=False)
    contact = models.CharField(max_length=18 , null=False)
    # college = models.CharField(max_length= 100, null=False)
    def __str__(self):
        return self.user.email
    
class Event(models.Model):
    """
    Model representing an event.
    """
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=2000, null=False)
    rules = models.CharField(max_length=4000, null=True)
    venue = models.CharField(max_length=50, null=False, default='B315')
    date = models.DateField(help_text='Mention (start) date of the event', default='2018-02-09')

    CAT = (
        ('c', 'cultural'),
        ('s', 'sports'),
        ('t', 'technical'),
    )
    category = models.CharField(max_length=1, choices=CAT, blank=False, default='c', help_text='category of event eg. Sports, Cultural, Technical')
    subCategory = models.CharField(max_length=50, help_text='In lowercase, without any space. e.g. music, drama')
    subCategoryName = models.CharField(max_length=50, help_text='Proper name of subcategory. eg. Music, Business and Entrepreneurship', default='')
    parentClub = models.CharField(max_length=50, help_text='eg Snuphoria,TEDx,')

    prize = models.DecimalField(help_text='Prize Money for the event',decimal_places=2, max_digits=8, null=True)
    fee = models.DecimalField(help_text='Registration fee for the event',decimal_places=2, max_digits=8, null=True)
    FEE_TYPE = (
        ('head', 'Per Head'),
        ('team', 'Per Team'),
    )
    fee_type = models.CharField(max_length=4, choices=FEE_TYPE, blank=False, default='head', help_text='type of pricing. Per head or per team')
#contact details
    phone_regex = RegexValidator(regex=r'\d{10}$')

    contact_market = models.CharField(max_length=50, help_text='Name of Contact representative', blank=True)
    phone_market = models.CharField(validators=[phone_regex], max_length=10, blank=True, help_text='Contact representative phone number')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s by %s'%(self.name,self.parentClub)


class AccPackage(models.Model):
    """
    Model representing an accomodation package.
    """
    name = models.CharField(max_length=200, null=False)
    fee = models.DecimalField(
        help_text='Fee of the package', decimal_places=2, max_digits=8, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Registration(models.Model):
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    payable = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    college = models.CharField(max_length=200, null=False, default='')
    registration_id = models.CharField(max_length=200, unique=True, default='')
    STATUS = (
        ('p', 'Paid'),
        ('u', 'Unpaid'),
    )
    transaction_status = models.CharField(max_length=1, choices=STATUS, blank=False, default='u')
    def __str__(self):
    	return '%s %s' % (self.registration_id, self.payable)

class AccomRegistration(models.Model):
    packageId = models.ForeignKey(AccPackage, on_delete=models.CASCADE, null=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    number = models.DecimalField(decimal_places=0, max_digits=3, null=True)
    days = models.DecimalField(decimal_places=0, max_digits=1, null=True)
    payable = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    college = models.CharField(max_length=200, null=False, default='')
    registration_id = models.CharField(max_length=200, unique=True, default='')
    STATUS = (
        ('p', 'Paid'),
        ('u', 'Unpaid'),
    )
    transaction_status = models.CharField(max_length=1, choices=STATUS, blank=False, default='u')
    def __str__(self):
    	return '%s %s' % (self.registration_id, self.payable)

class Formdata(models.Model):
    name= models.CharField(max_length = 32, null=False)
    age= models.IntegerField(default=0, null=True)
    gender= models.CharField(max_length=2, null=True)
    registration = models.ForeignKey(Registration, on_delete= models.CASCADE, null=False)
    def __str__(self):
        return self.registration


class ForgetPass(models.Model):
    token = models.CharField(max_length=64, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.user.email
