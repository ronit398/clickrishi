__author__ = "Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"
__credits__ = ["Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"]
__version__ = "1.0.1"
__maintainer__ = "Ronit Shrivastava"
__email__ = "clickrishiteam@gmail.com"
__status__ = "Production"

from django.contrib import admin
from .models import userprofile

admin.site.register(userprofile)
