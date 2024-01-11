from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header='Personal Porfolio Manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/',include('project.urls')),
    path('',include('django.contrib.auth.urls')),
    path('',include('members.urls'))
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
