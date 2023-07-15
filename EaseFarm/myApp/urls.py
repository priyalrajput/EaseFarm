from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('address', views.address, name='address'),
    path('BorrowProduct/', views.BorrowProduct, name='BorrowProduct'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    #path('minuscart/', views.minus_cart, name='minus_cart'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('static-Product-Detail/', views.static_Product_Detail, name='static-Product-Detail'),
    path('static-Product-Detail1/', views.static_Product_Detail1, name='static-Product-Detail1'),
    path("signup", views.CustomerRegistrationView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name= 'login.html', authentication_form = LoginForm), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path("Become_supplier", views.Become_supplier, name="Become_supplier"),
    path("password_reset", views.password_reset, name='password_reset'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("change_password/", auth_views.PasswordChangeView.as_view(template_name='change_password.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='change_password'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", form_class=MyPasswordResetForm), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html", form_class=MySetPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),

    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
]
