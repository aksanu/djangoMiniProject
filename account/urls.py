from django.urls import path
from . import views

urlpatterns = [
	path('profile',views.show_profile,name='show_profile'),
	path('signup',views.signup,name='signup'),
	path('profile/<int:user_id>', views.edit_email,name='edit_email'),
]