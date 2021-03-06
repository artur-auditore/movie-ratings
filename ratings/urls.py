from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('users/', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('starrings', StarringList.as_view(), name=StarringList.name),
    path('starrings/<int:pk>', StarringDetail.as_view(), name=StarringDetail.name),
    path('titles', TitleList.as_view(), name=TitleList.name),
    path('titles/<int:pk>', TitleDetail.as_view(), name=TitleDetail.name),
    path('genders', GenderList.as_view(), name=GenderList.name),
    path('genders/<int:pk>', GenderDetail.as_view(), name=GenderDetail.name),
    path('starring-titles', TitleStarringList.as_view(), name=TitleStarringList.name),
    path('profiles', ProfileList.as_view(), name=ProfileList.name),
    path('profiles/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),
    path('ratings', RatingList.as_view(), name=RatingList.name),
    path('ratings/<int:pk>', RatingDetail.as_view(), name=RatingDetail.name),
    path('api-token-auth', obtain_auth_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]