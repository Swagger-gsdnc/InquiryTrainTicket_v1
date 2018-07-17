#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""命令行火车查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2018-07-17
    tickets -dg 北京 上海 2018-07-17
"""
###docdtring前面不能有命令行
import requests
from docopt import docopt
from TrainsCollection import TrainsCollection

from stations import stations

def cli():
    """command-line interface"""
    arguements = docopt(__doc__)
    from_station = stations.get(arguements['<from>'])
    to_station = stations.get(arguements['<to>'])
    date = arguements['<date>']
    #构建URL
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
    '''
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-30&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
    #添加verify=False参数不验证证书
    print(url)
    r = requests.get(url)
    print(r.json())
    '''
    
    #获取参数
    options = ''.join([
        key for key,value in arguements.items() if value is True])
    r = requests.get(url)#, verify=False)
    available_trains = r.json()['data']['result']
    #key,value = enumerate(available_trains[0].split('|'))
    
    TrainsCollection(available_trains, options).pretty_print()

if __name__ == '__main__':
    cli()

