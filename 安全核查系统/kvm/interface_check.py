# coding:utf-8

from kvm.run import KVM_Benchmark_Main
from kvm import common
import json

def main(configure = '', rule = None, server = '10.108.115.216',port = 3306, user = 'cjb', password='1202' ):
    if not rule:
        rule = common.defaultRule
    kvmBenchmark = KVM_Benchmark_Main(rule=rule, server=server, port=port, user=user, password=password)
    return kvmBenchmark.getJsonResult().replace("\n", "")

def manualCheck():
    resList = []
    res = common.reportContent
    for i in range(len(common.ManualRule)):
        if common.ManualRule[i] == 0:
            resList.append({"index": common.reportIndex[i], "data": res[common.reportIndex[i]]})
    resJSON = json.dumps(resList, ensure_ascii=False, indent=7)
    return resJSON

if __name__ == "__main__":
    str = main(configure='', rule=None, server='10.108.115.134', port=22, user='root', password='12345678')
    print(str)
