from django.urls import path
from .views import SingUpView, ProfileUpdate, EmailUpdate, SingUpView2

urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('signup/2', SingUpView2.as_view(), name="signup2"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
]