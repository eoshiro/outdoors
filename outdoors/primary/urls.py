from django.urls import path
from primary import views
from django.conf import settings
from django.conf.urls.static import static



# Template Tagging
app_name = 'primary'

urlpatterns = [
    path('index/',views.ProjecttwoView.as_view(),name='contact'),
    path('',views.ProjecttwoView.as_view(),name='contact'),
    path('projecttwo/',views.ProjecttwoView.as_view(),name='projecttwo'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
