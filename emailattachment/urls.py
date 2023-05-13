from django.contrib import admin
from django.urls import path
from emailattachment_app import views
from django.conf import settings
from django.conf.urls.static import static
from emailattachment_app.views import generate_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('emailsend/',views.emailsend,name='emailsend'),
    path('signup/',views.signup,name='signup'),
    path('forgot_username/',views.forgot_username ,name='forgot_username'),
    path('forgot_otp/',views.forgot_otp ,name='forgot_otp'),
    path('forgot_password/',views.forgot_password ,name='forgot_password'),
    path('logout/',views.logout, name='logout'),
    path('generate_text/', generate_text, name='generate_text'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
        
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
