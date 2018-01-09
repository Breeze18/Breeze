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
    rules = models.CharField(max_length=2000, null=True)
    venue = models.CharField(max_length=50, null=False, default='B315')
    date = models.DateField(help_text='Mention (start) date of the event', default='2018-02-09')

    CAT = (
        ('c', 'cultural'),
        ('s', 'sports'),
        ('t', 'technical'),
    )
    category = models.CharField(max_length=1, choices=CAT, blank=False, default='c', help_text='category of event eg. Sports, Cultural, Technical')
    subCategory = models.CharField(max_length=50, help_text='eg Gaming,Dance,Music,Miscellaneous')
    parentClub = models.CharField(max_length=50, help_text='eg Snuphoria,TEDx,')

    prize = models.DecimalField(help_text='Prize Money for the event',decimal_places=2, max_digits=8, null=True)
    fee = models.DecimalField(help_text='Registration fee for the event',decimal_places=2, max_digits=8, null=True)

#contact details
    phone_regex = RegexValidator(regex=r'\d{10}$')

    contact_market = models.CharField(max_length=50, help_text='Marketing representative', null=True)
    phone_market = models.CharField(validators=[phone_regex], max_length=10, blank=True, help_text='Marketing representative phone number')

    contact_spons = models.CharField(max_length=50, help_text='Sponsorship representative', null=True)
    phone_spons = models.CharField(validators=[phone_regex], max_length=10, blank=True, help_text='Sponsorship representative phone number')

    contact_pr = models.CharField(max_length=50, help_text='PR representative', null=True)
    phone_pr = models.CharField(validators=[phone_regex], max_length=10, blank=True,  help_text='PR Representative phone number')


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s by %s'%(self.name,self.parentClub)


class Registration(models.Model):
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    transaction_id=models.CharField(max_length = 200, default="Unpaid")
    def __str__(self):
    	return '%s by %s'%(self.eventId,self.userId)

class Formdata(models.Model):
    name= models.CharField(max_length = 32, null=False)
    age= models.IntegerField(default=0, null=True)
    gender= models.CharField(max_length=2, null=True)
    registration = models.ForeignKey(Registration, on_delete= models.CASCADE, null=False)
    def __str__(self):
        return self.registration


class ForgetPass(models.Model):
    token = models.CharField(max_length=64, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
