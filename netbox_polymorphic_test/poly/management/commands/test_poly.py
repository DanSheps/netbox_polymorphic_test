from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):

    def handle(self, *args, **options):
        from poly.models import Region, Site, SiteGroup, Location, Device

        timing = {'create': {}, 'query': {}}
        try:
            with transaction.atomic():
                start = datetime.now()
                for i in range(1, 10):
                    region = Region.objects.create(name=f'Region {i}', code=f'C')
                    for j in range(1, 10):
                        site_group = SiteGroup.objects.create(parent=region, name=f'Region{i} Site Group{j}', code=f'D')
                        site = SiteGroup.objects.create(parent=site_group, name=f'Region {i} Site {j}', code=f'D')
                        for k in range(1, 10):
                            location = Location.objects.create(parent=site, name=f'Region {i} Site {j} Location {k}', code='S')
                            for l in range(1, 10):
                                device = Device.objects.create(
                                    name=f'Region {i} Site {j} Location {k} Device {l}',
                                    location=location
                                )
                end = datetime.now()
                timing['create'] = {'start': start, 'end': end, 'time': end-start}

                start = datetime.now()
                devices = Device.objects.all().prefetch_related('location')
                for device in devices:
                    data = f'Device: {device.name}, location={device.location.name}, site_group={device.location.get_ancestors()}'
                    # print(data)
                end = datetime.now()
                timing['query'] = {'start': start, 'end': end, 'time': end - start}

                print(f'Creation Timing: {timing.get("create", {}).get("time")}')
                print(f'Query Timing: {timing.get("query", {}).get("time")}')

                raise Exception('Reverting')
        except:
            pass
