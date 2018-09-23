from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from django.conf.urls.static import static
import jobs_app.views 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('home', jobs_app.views.home, name='home'),
    url('blog/', include('blog_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)