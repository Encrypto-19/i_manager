from django.urls import path
from . views import InfoListView, InfoCreateView, UserInfoListView, InfoDetailView, InfoUpdateView

urlpatterns = [
    path('', InfoListView.as_view(), name='i_blog_home'),
    path('i_blog/new/', InfoCreateView.as_view(template_name='i_blog/create.html'), name='i_blog_create'),
    path('i_blog/update/<int:pk>', InfoUpdateView.as_view(template_name='i_blog/update.html'), name='i_blog_update'),
    path('i_blog/userinfo/', UserInfoListView.as_view(template_name='i_blog/userinfo.html'), name='i_blog_userinfo'),
    path('i_blog/info_detail/<int:pk>/', InfoDetailView.as_view(template_name='i_blog/info_detail.html'), name = 'i_blog_infodetail'),
]