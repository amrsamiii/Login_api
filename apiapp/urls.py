from django.contrib import admin
from django.urls import path,include
from apiapp.views import awsImageview
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from . import views

# router= DefaultRouter()
# router.register('awsimages',awsImageview)
# urlpatterns = router.urls
# path('aws',include(router.urls))
router = DefaultRouter()
#router.register(r'product', ProductViewSet, basename='Product')
router.register(r'awsimages', awsImageview, basename='Image')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('auth.urls')),
   path('', include(router.urls)),


 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

