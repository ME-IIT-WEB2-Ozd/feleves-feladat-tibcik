from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import MedicineViewSet, PatientViewSet, TestViewSet, TestedViewSet, TreatmentViewSet, get_needed_tests, test_patient, get_last_test

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
router.register('treatments', TreatmentViewSet, basename='treatments')
router.register('medicines', MedicineViewSet, basename='medicines')
router.register('tests', TestViewSet, basename='tests')
router.register('testeds', TestedViewSet, basename='testeds')

urlpatterns = [
    path('testeds/test/', test_patient, name='test'),
    path('tests/get_needed_tests/<int:patient>/', get_needed_tests, name='get_needed_tests'),
    path('tests/get_last_test/', get_last_test, name='get_last_test'),
    path('', include(router.urls))
]