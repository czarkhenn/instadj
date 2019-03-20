from django.conf.urls import url
from django.urls import path
from .views import ajax
from .views import general

app_name = 'instaapp'
urlpatterns = [
    url(r'^$', general.index, name='index'),
    url(r'^login/$', general.user_login, name='user_login'),
    url(r'^viewprofile/$', general.viewprofile, name='viewprofile'),
    url(r'^home/$', general.home, name='home'),
    url(r'^logout/$', general.user_logout, name='user_logout'),
    url(r'^upload/$', general.upload_photo, name='upload_photo'),
    url(r'^users/$', general.users, name='users'),
    url(r'^signup/$', general.signup, name='signup'),
    url(r'^u/(?P<username>[\w-]+)$', general.user_profile, name='user_view'),
    url(r'^profile/$', general.user_profile, name='user_profile'),
    url(r'^following/$', general.user_following, name='user_following'),
    url(r'^followers/$', general.user_followers, name='user_followers'),
    url(r'^feed/$', general.feed, name='feed'),
    url(r'^search/$', general.search, name='user_search'),

    # AJAX methods
    url(r'^upload_dp/$', ajax.upload_user_profile_pic,
        name='upload_user_profile_pic'),
    url(r'^follow/$', ajax.follow_user, name='follow_user'),
    url(r'^unfollow/$', ajax.unfollow_user, name='unfollow_user'),
    url(r'^post_comment/$', ajax.post_photo_comment, name='post_photo_comment'),
    url(r'^like_comment/$', ajax.like_photo, name='like_photo'),
]
