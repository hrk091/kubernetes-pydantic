# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2022-03-30T02:38:35+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1
from . import v1 as v1_2


class CronJobStatus(BaseModel):
    class Config:
        allow_population_by_field_name = True

    active: Optional[List[v1.ObjectReference]] = Field(
        None, description='A list of pointers to currently running jobs.'
    )
    last_schedule_time: Optional[v1_1.Time] = Field(
        None,
        alias='lastScheduleTime',
        description='Information when was the last time the job was successfully scheduled.',
    )
    last_successful_time: Optional[v1_1.Time] = Field(
        None,
        alias='lastSuccessfulTime',
        description='Information when was the last time the job successfully completed.',
    )


class JobTemplateSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True

    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[v1_2.JobSpec] = Field(
        None,
        description='Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )


class CronJobSpec(BaseModel):
    class Config:
        allow_population_by_field_name = True

    concurrency_policy: Optional[str] = Field(
        None,
        alias='concurrencyPolicy',
        description='Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn\'t finished yet; - "Replace": cancels currently running job and replaces it with a new one',
    )
    failed_jobs_history_limit: Optional[int] = Field(
        None,
        alias='failedJobsHistoryLimit',
        description='The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.',
    )
    job_template: JobTemplateSpec = Field(
        ..., alias='jobTemplate', description='Specifies the job that will be created when executing a CronJob.'
    )
    schedule: str = Field(..., description='The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.')
    starting_deadline_seconds: Optional[int] = Field(
        None,
        alias='startingDeadlineSeconds',
        description='Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.',
    )
    successful_jobs_history_limit: Optional[int] = Field(
        None,
        alias='successfulJobsHistoryLimit',
        description='The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 3.',
    )
    suspend: Optional[bool] = Field(
        None,
        description='This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.',
    )
    time_zone: Optional[str] = Field(
        None,
        alias='timeZone',
        description='The time zone for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will rely on the time zone of the kube-controller-manager process. ALPHA: This field is in alpha and must be enabled via the `CronJobTimeZone` feature gate.',
    )


class CronJob(BaseModel):
    class Config:
        allow_population_by_field_name = True

    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[CronJobSpec] = Field(
        None,
        description='Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )
    status: Optional[CronJobStatus] = Field(
        None,
        description='Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )


class CronJobList(BaseModel):
    class Config:
        allow_population_by_field_name = True

    api_version: Optional[str] = Field(
        None,
        alias='apiVersion',
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[CronJob] = Field(..., description='items is the list of CronJobs.')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata',
    )
