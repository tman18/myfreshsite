from django.urls import path

import views

urlpatterns = [
    path('', views.index),
    path('about-me', views.about_me),
    path('resume', views.resume),
    path('contact', views.contact),
]

# Boilerplate to include static files.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static('static/', document_root=settings.STATIC_ROOT)