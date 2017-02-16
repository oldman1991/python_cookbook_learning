# coding=utf-8
import csv
import re

import tablib
import unicodedata


def unvisible_pattern():
    # \x00-\x1f\x7f 不可见的ascii码
    # \ue000-\uf8ff\u000f0000-\u000ffffd\u00100000-\u0010fffd Private Use Area
    return re.compile(u'[\x00-\x1f\x7f\uffff]')


def pua_process(s):
    s0 = ''
    for i in range(len(s)):
        if unicodedata.category(s[i]) == 'Co':
            continue
        s0 += s[i]
    return s0


def strformat(s):
    s = re.sub(unvisible_pattern(), '', s)
    # s = pua_process(s)
    if s.startswith('='):
        s = '\'' + s
    return s


def handler():
    csv_reader = csv.reader(open('1.csv', encoding='utf-8'))
    i=0
    dt_result = tablib.Dataset()
    dt_result.headers=[
        u'订单id', u'订单状态',
        u'付款时间', u'验证时间',
        u'美购id', u'美购名称',
        u'医生id', u'医生姓名', u'医院id', u'医院名称', u'所在城市',
        u'订单总价', u'预付款', u'实际线上付款', u'保险金额', u'美券抵扣金额', u'美分抵扣金额', u'抽成金额',
        u'付款商务id', u'付款商务姓名', u'付款商务分组',
        u'验证商务id', u'验证商务姓名', u'验证商务分组'
    ]
    list_result = []
    for row in csv_reader:
        #if i == 50000:
        #    break
        row_result = [strformat(item)for item in row]
        list_result.append(row_result)
        # print(row_result)row
        print(i)
        i += 1
    #dt_result.extend(list_result[:50000])
    dt_result.extend(list_result[:])
    #import pdb; pdb.set_trace()
    open(u'商务绩效.xlsx', 'wb').write(dt_result.xlsx)


if __name__ == '__main__':
    handler()
