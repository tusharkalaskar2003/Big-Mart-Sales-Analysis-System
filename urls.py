from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preference', views.preference, name='preference'),
    path('product_analysis', views.product_analysis, name='product_analysis'),
    path('product_analysis/<str:name>/', views.product_analysis, name='product_analysis'),
    path('store_analysis',views.store_analysis,name='store_analysis'),
    path('store_analysis/<str:name>/', views.store_analysis, name='store_analysis'),
    # path('homelander',views.outletSalesOfEachStore,name='homelander'),
    # path('superman/',views.locationAnalysisOfStore,name='superman'), 
    # path('bruce_wyane/',views.storeContributionAnalysis,name='bruce_wyane'),
    # path('bullyMaguire/',views.storeProductAnalysis,name='bullyMaguire'),
    # path('suparwayam_swami/',views.saleByRegions,name='suparwayam_swami'),
]
