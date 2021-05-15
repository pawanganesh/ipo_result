from django.urls import path

from .views import companyList_view, resultCheck_view, results_view, beneficiaryDetails_view, beneficiary_delete_view

app_name = 'ipo'
urlpatterns = [
    path('companylist/', companyList_view, name='company_list'),
    path('checkresult/', resultCheck_view, name='checkresult'),
    path('results/<int:companyShareId>/', results_view, name='results'),
    path('beneficiarydetails/', beneficiaryDetails_view, name='beneficiarydetails'),
    path('beneficiarydetails/<int:b_id>/', beneficiaryDetails_view, name='editbeneficiarydetails'),
    path('deletebeneficiary/<int:b_id>/', beneficiary_delete_view, name='deletebeneficiary'),
]
