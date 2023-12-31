from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class FilterCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'name']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = FilterCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        institution = CertifyingInstitution.objects.create(**validated_data)
        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=institution, **certificate_data
            )
        return institution
