from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, about
import debug_toolbar

urlpatterns = [
                  path('__debug__', include(debug_toolbar.urls)),
                  path('about/', about, name='about'),
                  path('admin/', admin.site.urls),
                  path('', include('userprofile.urls')),
                  path('', include('store.urls')),
                  path('', frontpage, name='frontpage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

