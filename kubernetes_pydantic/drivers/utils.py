from os import getenv

from kubernetes import client, config
from kubernetes.client import Configuration


def k8s_config() -> Configuration:
    conf = client.Configuration()
    if getenv("KUBECONFIG") is not None:
        config.load_kube_config(client_configuration=conf)
    else:
        config.load_incluster_config(client_configuration=conf)
    return conf
