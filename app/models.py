from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image


class Service(MPTTModel):
    name = models.CharField(max_length=128, null=False, blank=False)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_parents(self):
        parents = []
        p = self.parent
        while p:
            parents.append(p)
            p = p.parent
        parents.reverse()
        return parents

    def __str__(self):
        return f"{self.name}"


class Agent(models.Model):
    first_name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Prénom")
    last_name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Nom")
    police_number = models.IntegerField(blank=True, null=True, unique=True, verbose_name="Matricule")
    police_rank = models.CharField(max_length=64, blank=True, null=False, verbose_name="Grade")
    image = models.ImageField(blank=True, null=True)

    class Role(models.TextChoices):
        CHEF = 'Chef'
        ADJOINT = 'Adjoint'
        SECRETAIRE = 'Secrétaire'
        AUTRE = 'Autre'

    service = models.ForeignKey(to=Service, on_delete=models.CASCADE, blank=False, null=False, related_name="agents")
    role = models.CharField(choices=Role.choices, default=Role.AUTRE, blank=False, null=False,
                            max_length=32, verbose_name="Rôle")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
