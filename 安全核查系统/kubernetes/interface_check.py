# coding:utf-8

from kubernetes.run import Kubernetes_Benchmark_Main
#from run import Kubernetes_Benchmark_Main
import json

def main(server, user, password, port, type, configure = ''):
    # type: (object, object, object, object, object, object) -> object
    k8sBenchmark = Kubernetes_Benchmark_Main(server=server, user=user, password=password, port=port, nodetype=type)
    return k8sBenchmark.getJsonResult().replace("\n", "")
