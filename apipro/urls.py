from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

from apiapp import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from apiapp.views import awsImageview


router= DefaultRouter()

router.register('awsimages',awsImageview)


# router.register(r'image', ImageViewSet, basename='Image')
from django.urls import path
from apiapp.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from apiapp import views

# 
# router = DefaultRouter()
# router.register(r'awsimages', awsImageview, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('register/', userSignupViewset.as_view(), name='auth_register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rest/Diseases/',views.FBV_LIST),
    path('rest/Fertilizers/',views.fer_list),
    path('rest/Ret/',views.ret),
    # path('awsimage',awsImageview.as_view(),name='aws_image'),
    # path('auth/', include('auth.urls')),
    # path('', include(router.urls)),
     path('',include(router.urls))

]
# urlpatterns+=router.urls
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
