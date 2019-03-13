import json
import math
import argparse
import requests


def get_arguments_from_user():
    parse = argparse.ArgumentParser(
        prog='BarsProgramm', description='Some test functionality')

    parse.add_argument('--file_path', default='bars.json',
                       help='Если в дериктории со скриптом нет файла со'
                       'списком баров, то тут можно указать путь до файла.'
                       'Или скачать его по ссылке : https://devman.org/fshare/1503831681/4/')

    return parse.parse_args()


url = 'https://yandex.ru'
response = requests.get(url)
print(response.headers)

gafu = get_arguments_from_user()
print(gafu.file_path)
with open(gafu.file_path, "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
    # print(data['features'][:1])
    bars = data['features']
    # Bar_Name = str
    # def biggest_bar(data):

    def get_longitude_latitude(bar):
        return bar['geometry']['coordinates']

    print('Smallest', min(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
          ['properties']['Attributes']['Name'])
    Small_Bar = int(bars[1]['properties']['Attributes']['SeatsCount'])
    print(min(bars, key=lambda x: math.hypot(
        (get_longitude_latitude(x)[0] - 1), (get_longitude_latitude(x)[1] - 1)))['properties']['Attributes']['Name'])
    # print(Small_Bar['properties']['Attributes']['SeatsCount'])
    i = 0
    for bar in bars:
        # print(get_longitude_latitude(bar)[1])
        longitude_latitude = bar['geometry']['coordinates']
        # print(type(longitude_latitude))
        if Small_Bar > bar['properties']['Attributes']['SeatsCount']:
            Small_Bar = bar['properties']['Attributes']['SeatsCount']
            Bar_Name = bar['properties']['Attributes']['Name']
        # elif Small_Bar == bar['properties']['Attributes']['SeatsCount']:
            # i = i + 1
    Smallest_Bars = []
    for bar in bars:
        if Small_Bar == bar['properties']['Attributes']['SeatsCount']:
            Smallest_Bars.append(bar['properties']['Attributes']['Name'])
    # print(Bar_Name)
    for Bar in Smallest_Bars:
        print(Bar)
    # print(i)
