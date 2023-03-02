from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField


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
    image = models.ImageField(blank=True, null=True)
    grade = models.CharField(max_length=64, blank=True, null=False, verbose_name="Grade")
    registration_number = models.IntegerField(blank=True, null=True, unique=True, verbose_name="Matricule")
    phone = PhoneNumberField(null=True, blank=True, region="FR", verbose_name="Poste fixe")
    mobile = PhoneNumberField(null=True, blank=True, region="FR", verbose_name="Mobile")

    class Role(models.TextChoices):
        CHEF = 'Chef'
        ADJOINT = 'Adjoint'
        SECRETAIRE = 'Secrétaire'
        AUTRE = 'Autre'

    service = models.ForeignKey(to=Service, on_delete=models.CASCADE, blank=False, null=False, related_name="agents")
    role = models.CharField(choices=Role.choices, default=Role.AUTRE, blank=False, null=False,
                            max_length=32, verbose_name="Rôle")

    IMAGE_MAX_SIZE = (283, 377)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()

    def has_informations(self):
        if self.grade or self.registration_number or self.phone or self.mobile:
            return True
        return False

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
