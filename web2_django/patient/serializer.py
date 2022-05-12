from rest_framework import serializers

from .models import Patient, Treatment, Medicine, Test, Tested

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'name',
            'szul_date',
            'taj',
            'nem'
        )

class TreatmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Treatment
        fields = (
            'id',
            'patient',
            'kezeles',
            'ido'
        )

class MedicineSerializer(serializers.ModelSerializer):
    treatment = TreatmentSerializer(read_only=True)

    class Meta:
        model = Medicine
        fields = (
            'treatment',
            'gyogyszer'
        )

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id',
            'name',
            'nem',
            'kor',
            'interval'
        )

class TestedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    test = TestSerializer(read_only=True)

    class Meta:
        model = Tested
        fields = (
            'patient',
            'test',
            'utolso'
        )