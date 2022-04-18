from typing import Callable

from src.drivers.apicore import K8sApiCore


class CronJobApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.batchv1.create_namespaced_cron_job

    @property
    def merger(self) -> Callable:
        return self.api.batchv1.patch_namespaced_cron_job

    @property
    def replacer(self) -> Callable:
        return self.api.batchv1.replace_namespaced_cron_job

    @property
    def deleter(self) -> Callable:
        return self.api.batchv1.delete_namespaced_cron_job

    @property
    def lister(self) -> Callable:
        return self.api.batchv1.list_namespaced_cron_job

    @property
    def getter(self) -> Callable:
        return self.api.batchv1.read_namespaced_cron_job


class JobApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.batchv1.create_namespaced_job

    @property
    def merger(self) -> Callable:
        return self.api.batchv1.patch_namespaced_job

    @property
    def replacer(self) -> Callable:
        return self.api.batchv1.replace_namespaced_job

    @property
    def deleter(self) -> Callable:
        return self.api.batchv1.delete_namespaced_job

    @property
    def lister(self) -> Callable:
        return self.api.batchv1.list_namespaced_job

    @property
    def getter(self) -> Callable:
        return self.api.batchv1.read_namespaced_job
