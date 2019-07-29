from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from website import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax_calls/myFunction/', views.getnamesview,name='getname'),
    url(r'^logout/$',views.Logout,name='logout'),
    url(r'^action/$',views.Actions,name='action'),
    url(r'^adventure/$',views.Adventures,name='adventures'),
    url(r'^animation/$',views.Animations,name='animations'),
    url(r'^children/$',views.Childrens,name='childrens'),
    url(r'^comedy/$',views.Comedys,name='comedys'),
    url(r'^crime/$',views.Crimes,name='crimes'),
    url(r'^documentary/$',views.Documentarys,name='documentarys'),
    url(r'^drama/$',views.Dramas,name='dramas'),
    url(r'^fantasy/$',views.Fantasys,name='fantasys'),
    url(r'^filmnoir/$',views.Filmnoirs,name='filmnoirs'),
    url(r'^horror/$',views.Horrors,name='horrors'),
    url(r'^musical/$',views.Musicals,name='musicals'),
    url(r'^mystery/$',views.Mysterys,name='mysterys'),
    url(r'^romance/$',views.Romances,name='romances'),
    url(r'^scifi/$',views.Scifis,name='scifis'),
    url(r'^thriller/$',views.Thrillers,name='thrillers'),
    url(r'^war/$',views.Wars,name='wars'),
    url(r'^western/$',views.Westerns,name='westerns'),
    url(r'^movie/$',views.Movie,name='movie'),
    url(r'^movie/cart/$',views.cart,name='cart'),
    url(r'^movie/delete/$',views.delete,name='delete'),
    url(r'^movie/recommend/$',views.recommend,name='recommend'),
    url(r'^movie/cf/$',views.cf,name='cf'),
    url(r'^movie/item/$',views.item,name='iten'),
    url(r'^movie/arm/$',views.arm,name='arm'),
    url(r'^history/$',views.history,name='history'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^$',views.Login,name='login'),
    
    ] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)