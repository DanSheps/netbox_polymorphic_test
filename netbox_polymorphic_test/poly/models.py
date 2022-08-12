from django.db import models
from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey


class BaseLocation(PolymorphicMPTTModel):
    parent = PolymorphicTreeForeignKey('self', blank=True, null=True, related_name='children', verbose_name='Parent', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = "Tree node"
        verbose_name_plural = "Tree nodes"


class Region(BaseLocation):
    code = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class SiteGroup(BaseLocation):
    code = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"


class Site(BaseLocation):
    code = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Site Group"
        verbose_name_plural = "Site Groups"


class Location(BaseLocation):
    code = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Device(models.Model):
    location = models.ForeignKey(to=BaseLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
