from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("plot",views.load_plot,name="plot"),
    path("", views.index, name="home"),
    path("about",views.load_about,name="about"),
    path("members",views.load_members,name="members"),
    path("output",views.load_output,name="output")
	]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)