from googleapiclient.discovery import Resource
from googleapiclient.errors import HttpError
from insightconnect_plugin_runtime.exceptions import PluginException


class GoogleCloudComputeAPI:
    def __init__(self, service: Resource, project_id: str):
        self.service = service
        self.project_id = project_id

    def get_firewall(self, firewall: str):
        request = self.service.firewalls().get(project=self.project_id, firewall=firewall)
        return self.execute(request)

    def list_firewalls(self, filter_=None, max_results=None, order_by=None):
        if not filter_:
            filter_ = None
        if not max_results:
            max_results = None
        if not order_by:
            order_by = None

        request = self.service.firewalls().list(
            project=self.project_id, filter=filter_, maxResults=max_results, orderBy=order_by
        )

        response = None
        items = []

        while request is not None:
            response = request.execute()
            items += response["items"]

            request = self.service.firewalls().list_next(previous_request=request, previous_response=response)

        response["items"] = items
        return response

    def insert_firewall(self, body: dict):
        request = self.service.firewalls().insert(project=self.project_id, body=body)
        return self.execute(request)

    def update_firewall(self, firewall: str, body: dict):
        request = self.service.firewalls().update(project=self.project_id, firewall=firewall, body=body)
        return self.execute(request)

    def delete_firewall(self, firewall: str):
        request = self.service.firewalls().delete(project=self.project_id, firewall=firewall)
        return self.execute(request)

    def disk_snapshot(self, zone: str, disk: str, snapshot_body: dict):
        request = self.service.disks().createSnapshot(project=self.project_id, zone=zone, disk=disk, body=snapshot_body)
        return self.execute(request)

    def delete_snapshots(self, snapshot: str):
        request = self.service.snapshots().delete(project=self.project_id, snapshot=snapshot)
        return self.execute(request)

    def disk_attach(self, zone: str, instance: str, source: str):
        attached_disk_body = {"source": source}

        request = self.service.instances().attachDisk(
            project=self.project_id, zone=zone, instance=instance, body=attached_disk_body
        )
        return self.execute(request)

    def disk_detach(self, zone: str, instance: str, device_name: str):
        request = self.service.instances().detachDisk(
            project=self.project_id, zone=zone, instance=instance, deviceName=device_name
        )
        return self.execute(request)

    def disk_list(self, zone: str, filter_=None, max_results=None, order_by=None):
        if not filter_:
            filter_ = None
        if not max_results:
            max_results = None
        if not order_by:
            order_by = None

        request = self.service.disks().list(
            project=self.project_id, zone=zone, filter=filter_, maxResults=max_results, orderBy=order_by
        )

        response = None
        items = []

        while request is not None:
            response = request.execute()
            items += response["items"]

            request = self.service.disks().list_next(previous_request=request, previous_response=response)

        response["items"] = items
        return response

    def start_instance(self, zone: str, instance: str):
        request = self.service.instances().start(project=self.project_id, zone=zone, instance=instance)
        return self.execute(request)

    def stop_instance(self, zone: str, instance: str):
        request = self.service.instances().stop(project=self.project_id, zone=zone, instance=instance)
        return self.execute(request)

    def list_instances(self, zone: str, filter_=None, max_results=None, order_by=None):
        if not filter_:
            filter_ = None
        if not max_results:
            max_results = None
        if not order_by:
            order_by = None

        request = self.service.instances().list(
            project=self.project_id, zone=zone, filter=filter_, maxResults=max_results, orderBy=order_by
        )

        response = None
        items = []

        while request is not None:
            response = request.execute()
            items += response["items"]

            request = self.service.instances().list_next(previous_request=request, previous_response=response)

        response["items"] = items
        return response

    def list_snapshots(self, filter_=None, max_results=None, order_by=None):
        if not filter_:
            filter_ = None
        if not max_results:
            max_results = None
        if not order_by:
            order_by = None

        request = self.service.snapshots().list(
            project=self.project_id, filter=filter_, maxResults=max_results, orderBy=order_by
        )

        response = None
        items = []

        while request is not None:
            response = request.execute()
            items += response["items"]

            request = self.service.snapshots().list_next(previous_request=request, previous_response=response)

        response["items"] = items
        return response

    def list_zones(self):
        request = self.service.zones().list(project=self.project_id)
        return self.execute(request)

    @staticmethod
    def execute(request):
        try:
            return request.execute()
        except HttpError as e:
            if e.resp.status == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=e)
            if e.resp.status == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=e)
            if e.resp.status == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=e)
            if 400 <= e.resp.status < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
            if e.resp.status >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=e)

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
