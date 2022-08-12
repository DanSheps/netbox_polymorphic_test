from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Region(MPTTModel):
    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        db_index=True
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=30)

    class Meta(MPTTModel.Meta):
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class SiteGroup(MPTTModel):
    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        db_index=True
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"


class Site(models.Model):
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE)
    group = models.ForeignKey(to=SiteGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=30)


    class Meta:
        verbose_name = "Site Group"
        verbose_name_plural = "Site Groups"


class Location(models.Model):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Device(models.Model):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Device"
