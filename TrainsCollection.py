#!/usr/bin/python
# -*- coding: UTF-8 -*-
from prettytable import PrettyTable
from colorama import init, Fore
from stations import stations

init() #colorama init

class TrainsCollection:
 
    header = '车次 车站 时间 历时 商务座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他'.split()
 
    def __init__(self, available_trains, options):
        """查询到的火车班次集合
        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options
    '''
    def _get_duration(self, raw_train):
        duration = raw_train.get('lishi').replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    '''
    @property
    def trains(self):
        for raw_train in self.available_trains:
            raw_train = raw_train.split('|')
            train_no = raw_train[3]
            initial = train_no[0].lower()
            for key,value in stations.items():
                if value == raw_train[6]:
                    from_station_name = key
                if value == raw_train[7]:
                    to_station_name = key
            if not self.options or initial in self.options:
                train = [
                    train_no,        
                    '\n'.join([Fore.GREEN+from_station_name+Fore.RESET,
                        Fore.RED+to_station_name+Fore.RESET]),
                    '\n'.join([Fore.GREEN+raw_train[8]+Fore.RESET,
                        Fore.RED+raw_train[9]+Fore.RESET]),
                    raw_train[10],#历时
                    raw_train[32],#特等
                    raw_train[31],#一等
                    raw_train[30],#二等
                    raw_train[21],#高级软卧
                    raw_train[23],#软卧
                    raw_train[33],#动卧
                    raw_train[28],#硬卧
                    raw_train[24],#软座
                    raw_train[29],#硬座
                    raw_train[26],#无座
                    raw_train[22],#其他
                ]
                for key,value in enumerate(train):
                    if value == '':
                        train[key] = '-'
                '''
                tickect.gaojiruanwo = temp[21];    // 高级软卧
                tickect.ruanwo = temp[23];    // 软卧
                tickect.ruanzuo = temp[24]; // 软座
                tickect.wuzuo = temp[26];    // 无座
                tickect.yingwo = temp[28];  // 硬卧
                tickect.yingzuo = temp[29]; // 硬座
                tickect.scSeat = temp[30];    // 二等座
                tickect.fcSeat = temp[31];    // 一等座
                tickect.bcSeat = temp[32];    // 商务座 / 特等座
                tickect.dongwo = temp[33];    // 动卧
                data['qt_num'] = temp[22];   #其他
                data['note_num'] = temp[1];  #备注在1号位置
                '''
                yield train
 
    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)
