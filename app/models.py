from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image


class Service(MPTTModel):
    name = models.CharField(max_length=128)
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
    first_name = models.CharField(max_length=64, verbose_name="Prénom")
    last_name = models.CharField(max_length=64, verbose_name="Nom")
    police_number = models.IntegerField(verbose_name="Matricule")
    police_rank = models.CharField(max_length=64, verbose_name="Grade")
    image = models.ImageField(null=True, blank=True)

    class Role(models.TextChoices):
        CHEF = 'Chef'
        ADJOINT = 'Adjoint'
        SECRETAIRE = 'Secrétaire'
        AUTRE = 'Autre'

    service = models.ForeignKey(to=Service, on_delete=models.CASCADE, related_name="agents")
    role = models.CharField(choices=Role.choices, default=Role.AUTRE, max_length=32, verbose_name="Rôle")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
