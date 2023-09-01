from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    github = models.URLField(blank=False)
    linkedin = models.URLField(blank=False)
    bio = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=500, blank=False)
    github_url = models.URLField(blank=False)
    keyword = models.CharField(max_length=50, blank=False)
    key_skill = models.CharField(max_length=50, blank=False)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=False)

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    profiles = models.ManyToManyField(
        Profile, related_name="certificates"
    )

    def __str__(self) -> str:
        return self.name
