from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=18 , null=False)
    # college = models.CharField(max_length= 100, null=False)
    def __unicode__(self):
        return self.user

class Event(models.Model):
    """
    Model representing an event.
    """
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=2000, null=False)

    CAT = (
        ('c', 'Cultural'),
        ('s', 'Sports'),
        ('t', 'Technical'),
    )
    category = models.CharField(max_length=1, choices=CAT, blank=False, default='c', help_text='category of event')

    subCategory = models.CharField(max_length=50, help_text='eg Dance,Music,')
    parentClub = models.CharField(max_length=50, help_text='eg Snuphoria,TEDx,')
    contact = models.CharField(max_length=500, help_text='contact person(s) details')
    def __unicode__(self):
        """
        String for representing the Model object.
        """
        return '%s by %s'%(self.name,self.parentClub)


class Registration(models.Model):
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    transaction_id=models.CharField(max_length = 200, default="Unpaid")
    def __unicode__(self):
    	return '%s by %s'%(self.eventId,self.userId)

class Formdata(models.Model):
    name= models.CharField(max_length = 32, null=False)
    age= models.IntegerField(default=0, null=True)
    gender= models.CharField(max_length=2, null=True)
    registration = models.ForeignKey(Registration, on_delete= models.CASCADE, null=False)
    def __unicode__(self):
        return self.registration
