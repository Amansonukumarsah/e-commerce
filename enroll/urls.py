from re import template
from django.urls import path
from .forms import loginform,passwordchange,setpassword,resetpassword
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homeview.as_view(),name='home'),
    path('productdetails/<int:pk>', views.productdetailsview.as_view(),name='productdetails'),

    # Electro....................
    path('electro/', views.electronicview.as_view(),name='elctro'),
    path('electro/<slug:data>', views.electronicview.as_view(),name='elctrodata'), 
    # Electro..........................


    # Jwellery.......................
    path('Jwellery/', views.jwelleryView.as_view(),name='jwellery'),
    path('Jwellery/<slug:data>', views.jwelleryView.as_view(),name='jwellerydata'), 
    # # Jwellery...............................


    # Belt.......................
    path('Belt/', views.BeltView.as_view(),name='Belt'),
    path('Belt/<slug:data>', views.BeltView.as_view(),name='Beltdata'), 
    # # Belt...............................

    # Babyclothes.......................
    path('Babyclothes/', views.BabyclothesView.as_view(),name='Babyclothes'),
    path('Babyclothes/<slug:data>', views.BabyclothesView.as_view(),name='Babyclothesdata'), 
    # # Babyclothes...............................


    # Comfortsofa.......................
    path('Comfortsofa/', views.ComfortsofaView.as_view(),name='Comfortsofa'),
    path('Comfortsofa/<slug:data>', views.ComfortsofaView.as_view(),name='Comfortsofadata'), 
    # # Comfortsofa...............................


    # Handbags.......................
    path('Handbags/', views.HandbagsView.as_view(),name='Handbags'),
    path('Handbags/<slug:data>', views.HandbagsView.as_view(),name='Handbagsdata'), 
    # # Handbags...............................


    # Shoes.......................
    path('Shoes/', views.ShoesView.as_view(),name='Shoes'),
    path('Shoes/<slug:data>', views.ShoesView.as_view(),name='Shoesdata'), 
    # # Shoes...............................


    # gift.......................
    path('gift/', views.giftView.as_view(),name='gift'),
    path('gift/<slug:data>', views.giftView.as_view(),name='giftdata'), 
    # # gift...............................


    path('register/', views.registrationformsview.as_view(),name='register'),  
    
    path('accounts/login/',auth_views.LoginView.as_view(template_name="enroll/login.html",authentication_form=loginform),name='login'), 
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name='logout') ,

    path("passwordchange/", auth_views.PasswordChangeView.as_view(template_name="enroll/changepassword.html",form_class=passwordchange), name="passwordchange"),
    path("passwordchange/done/", auth_views.PasswordChangeDoneView.as_view(template_name="enroll/passwordchangedone.html"), name="password_change_done"),
    
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="enroll/password_reset.html",form_class=resetpassword), name="password_reset"),

    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="enroll/password_reset_done.html"), name="password_reset_done"),

    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="enroll/password_reset_confirm.html",form_class=setpassword), name="password_reset_confirm"),

    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="enroll/password_reset_complete.html"), name="password_reset_complete"),

    path('profile/',views.profile,name='profile'),  
    path('Adress/',views.Adress,name='adress'),  
    path('empty/',views.empty,name='empty'),  

    path('cart/', views.addtocart,name='cart'),
    path('cart1/', views.show_cart,name='show_cart'),

    path('place/', views.placeorder,name='place'),
    path('payment/', views.payment,name='payment'),


    path('od/',views.order_details,name='order'),

    path('login_cart/',views.login_cart,name='login_cart'),

    path('reco/',views.Recommendation,name='reco'),
    path('contact/',views.contact,name='contact'),

    path('about/',views.About,name='about'),

# path("contact", views.contact, name="contact"),

    # path('review',views.Review,name='review'),  


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)