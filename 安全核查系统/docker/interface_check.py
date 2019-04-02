# coding:utf-8

from docker.run import Docker_Benchmark_Main
import json

def main(server, user, password, port, configure = ''):
    # type: (object, object, object, object, object, object) -> object
    docker = Docker_Benchmark_Main(server=server, user=user, password=password, port=port)
    return docker.get_json_result().replace("\n", "")
