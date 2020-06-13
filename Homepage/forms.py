__author__ = "Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"
__credits__ = ["Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"]
__version__ = "1.0.1"
__maintainer__ = "Ronit Shrivastava"
__email__ = "clickrishiteam@gmail.com"
__status__ = "Production"


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import userprofile




#Form to load the profile pic of the user
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ['profilepic',]