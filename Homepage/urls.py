"""Clickrishi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


__author__ = "Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"
__credits__ = ["Ronit Shrivastava, Aman Kumar mishra, Prabhash meharia, Kaushikk ghosh"]
__version__ = "1.0.1"
__maintainer__ = "Ronit Shrivastava"
__email__ = "clickrishiteam@gmail.com"
__status__ = "Production"



from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('instructions/',views.instructions,name="instructions"),
    path('Register/',views.Register,name="Register"),
    path('FAQs/',views.FAQs,name="FAQs"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('Aboutus/',views.Aboutus,name="Aboutus"),
    path('Login/',views.Login,name="Login"),
    path('standalone/',views.standalone,name="standalone"),
    path('standtohome/',views.standtohome,name="standtohome"),
    path('sendFeedback/',views.sendFeedback,name="sendFeedback"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
