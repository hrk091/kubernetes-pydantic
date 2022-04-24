from kubernetes import client, config
from kubernetes.client import Configuration


def k8s_config() -> Configuration:
    conf = client.Configuration()
    config.load_kube_config(client_configuration=conf)
    if conf.host == "http://localhost":
        config.load_incluster_config(client_configuration=conf)
    return conf
