"""psm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from psm.views import login, home, category, national_stock, update_stock, adjacent_district, notice, notice_details, \
    research_article, research_article_details, request_stock, requested_stock
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/login'}, name='logout'),
    path('', home, name='home'),
    path('category/<int:id>', category, name='category'),
    path('national_stock/<int:id>', national_stock, name='national_stock'),
    path('adjacent_stock/<int:district_id>/category/<int:id>', adjacent_district, name='adjacent_district'),
    path('update_stock/<int:id>', update_stock, name='update_stock'),
    path('<int:category_id>/notice/', notice, name='notice'),
    path('<int:category_id>/notice/<int:id>', notice_details, name='notice_details'),
    path('<int:category_id>/research_article/', research_article, name='research_article'),
    path('<int:category_id>/research_article/<int:id>', research_article_details, name='notice_details'),
    path('request_stock/<int:category_id>/district/<int:district_id>/item/<int:id>', request_stock,
         name='request_stock'),
    path('request_stock/<int:category_id>/district/item/<int:id>/', request_stock, name='request_stock'),
    path('requested_stock/<int:id>', requested_stock, name='requested_stock')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
