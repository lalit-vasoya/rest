from django.urls import path,include

from rest_framework.routers import DefaultRouter # use when viewset is used in our code

from profiles_api import views

router = DefaultRouter() #create object
router.register('hello-viewset',views.HelloViewSet,basename='hello-view') #register view for router
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view(),name='hello_view'),
    path('login/',views.UserLoginApiView.as_view(),name='login_view'),
    path('',include(router.urls)),
]
