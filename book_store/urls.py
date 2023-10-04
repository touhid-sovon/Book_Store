from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # user management
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('allauth.urls')),
    # local app
    # path('accounts/',include('accounts.urls')),
    path('',include('pages.urls')),
    path('books/',include('books.urls')),
 ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

if settings.DEBUG: # new
    import debug_toolbar
    
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

