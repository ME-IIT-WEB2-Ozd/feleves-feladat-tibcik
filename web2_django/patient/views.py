from datetime import date
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import PatientSerializer, TreatmentSerializer, MedicineSerializer, TestSerializer, TestedSerializer
from.models import Medicine, Patient, Test, Tested, Treatment

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class TreatmentViewSet(viewsets.ModelViewSet):
    serializer_class = TreatmentSerializer
    queryset = Treatment.objects.all()

    def retrieve(self, request, pk=None):
        tretments = self.queryset.filter(patient=pk).order_by('-ido')
        serializer = TreatmentSerializer(tretments, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.filter(patient=self.request.data['patient']).order_by('ido')

    def perform_create(self, serializer):
        patient = Patient.objects.filter(pk=self.request.data['patient']).first()

        serializer.save(patient=patient)

    def perform_update(self, serializer):
        return

    def perform_destroy(self, serializer):
        return

class MedicineViewSet(viewsets.ModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()

    def retrieve(self, request, pk=None):
        medicines = self.queryset.filter(treatment=pk)
        serializer = MedicineSerializer(medicines, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.filter(treatment=self.request.data['treatment'])

    def perform_create(self, serializer):
        treatment = Treatment.objects.filter(pk=self.request.data['treatment']).first()

        serializer.save(treatment=treatment)

    def perform_update(self, serializer):
        return

    def perform_destroy(self, serializer):
        return

class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

@api_view(['GET'])
def get_needed_tests(request, patient=None):
    patient = Patient.objects.filter(pk=patient).first()

    tests = Test.objects.filter(kor__lte=(date.today()-patient.szul_date).days/365, nem__in=("m", patient.nem))
    tests_ids = tests.values_list('id', flat=True)
    tests_interval = tests.values_list('interval', flat=True)
    testeds = Tested.objects.filter(patient=patient,test__in=tests_ids,utolso__gte=tests_interval).values_list('test', flat=True)

    needed_test = tests.exclude(id__in=testeds)

    serializer = TestSerializer(needed_test, many=True)

    return Response(serializer.data)

    test = Test.objects.filter(kor__gte=patient.szul_ido)

@api_view(['GET'])
def get_last_test(request):
    last_test = Tested.objects.filter(patient=request.data['patient'], test=request.data['test']).first()

    serializer = TestedSerializer(last_test)

    return Response(serializer.data)

class TestedViewSet(viewsets.ModelViewSet):
    serializer_class = TestedSerializer
    queryset = Tested.objects.all()

    def get_queryset(self):
        return self.queryset.filter(patient=self.request.data['patient'], test=self.request.data['test'])

    def perform_create(self, serializer):
        patient = Patient.objects.filter(pk=self.request.data['patient']).first()
        test = Test.objects.filter(pk=self.request.data['test']).first()

        serializer.save(patient=patient, test=test)

    def perform_update(self, serializer):
        return

    def perform_destroy(self, serializer):
        return

@api_view(['PUT'])
def test_patient(request):
    patient = Patient.objects.filter(pk=request.data['patient']).first()
    test = Test.objects.filter(pk=request.data['test']).first()
    tested = Tested.objects.filter(patient=patient, test=test).first()

    serializer = TestedSerializer(tested, data={})

    if serializer.is_valid():
        serializer.save(patient=patient, test=test)

    return Response(serializer.data)