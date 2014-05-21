from django.conf.urls import patterns, include, url
from mongoapp.views import CreateUserView
from django.contrib import auth


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^new','mongoapp.views.home'),
    url(r'createuser/',CreateUserView.as_view()),
	url(r'create/','mongoapp.views.Contact_Create',name='create_list'),
	url(r'users/all/','mongoapp.views.users',name='users_all'),
    url(r'login/','mongoapp.views.loginuser',name='login_user'),
    url(r'accounts/auth/','mongoapp.views.auth_view'),
    url(r'accounts/invalid/','mongoapp.views.invalid_login'),
    url(r'accounts/loggedin/','mongoapp.views.loggedin'),
    url(r'accounts/logout/','mongoapp.views.logout'),
    url(r'register/','mongoapp.views.register_user'),
    url(r'register_success/','mongoapp.views.register_success'),
    url(r'^get/(?P<user_id>[a-z 0-9\-]+)/$', 'mongoapp.views.particularuser'),
    url(r'^edit/(?P<user_name>[a-z 0-9\-]+)/$', 'mongoapp.views.edituser'),
    url(r'^delete/(?P<user_name>[a-z 0-9\-]+)/$', 'mongoapp.views.deleteuser'),
    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>[0-9A-Za-z\-].+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^getdistrict/$','mongoapp.views.getdistrict'),
    # Examples:
    # url(r'^$', 'mongoproject.views.home', name='home'),
    # url(r'^mongoproject/', include('mongoproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
