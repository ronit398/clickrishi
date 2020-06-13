__author__ = "Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"
__credits__ = ["Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"]
__version__ = "1.0.1"
__maintainer__ = "Ronit Shrivastava"
__email__ = "clickrishiteam@gmail.com"
__status__ = "Production"


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver



from django.db.models import signals


#User object model to store the Profile pic in the Database
class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profilepic = models.ImageField(default='default.png',upload_to='profile_pic',blank = True)


#Siganls To create the user object Instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile.objects.create(user=instance)

#Siganls To save the user object Instance
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()
