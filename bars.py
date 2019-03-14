import json
import math
import argparse
import sys
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as read_file:
        return json.load(read_file)['features']


def get_biggest_bar(json_file_data):
    return max(json_file_data, key=lambda x: x['properties']['Attributes']
               ['SeatsCount'])


def get_smallest_bar(json_file_data):
    return min(json_file_data, key=lambda x: x['properties']['Attributes']
               ['SeatsCount'])


def get_bar_longitude_latitude_coordinates(bar_data):
    return bar_data['geometry']['coordinates']


def get_closest_bar(json_file_data, longitude, latitude):
    return min(json_file_data, key=lambda x:
               math.hypot((get_bar_longitude_latitude_coordinates(x)[0]
                           - longitude),
                          (get_bar_longitude_latitude_coordinates(x)[1]
                           - latitude))
               )


def print_formatted_bar_name(masseg, bar_data):
    print('{0}\n{1}:\n{2}'.format(('-'*30), masseg, data
                                  ['properties']['Attributes']['Name']))


def get_console_args():
    parser = argparse.ArgumentParser(prog='Biggest, smallest, closest Bars',
                                     description='Count the closest, biggest'
                                     'and smallest bar from the json file.')

    parser.add_argument('--file_path', default='bars.json',
                        help="If you haven't got file bars.jason in the script"
                        "directory, specify the path for the file, or download"
                        "it from link:"
                        "https://devman.org/fshare/1503831681/4/")

    return parser.parse_args()


def input_your_latitude_longitude():
    try:
        latitude_longitude_list = [0.0, 0.0]
        latitude_longitude_list[0] = float(
            input('Введите широту Вашего местоположения:\n'))
        latitude_longitude_list[1] = float(
            input('Введите долготу Вашего местоположения:\n'))
        return latitude_longitude_list
    except ValueError:
        return None


if __name__ == '__main__':
    parse_args = get_console_args()
    json_file_data = load_data(parse_args.file_path)
    if json_file_data is None:
        sys.exit('Файл не найден или данные не в формате JSON')
    latitude_longitude_list = input_your_latitude_longitude()
    if latitude_longitude_list is None:
        sys.exit('Введено некорректное значение')

    print_formatted_bar_name(
        'Самый большой бар', get_biggest_bar(json_file_data))
    print_formatted_bar_name('Самый маленький бар',
                             get_smallest_bar(json_file_data))
    print_formatted_bar_name('Самый близкий бар',
                             get_closest_bar(json_file_data,
                                             latitude_longitude_list[0],
                                             latitude_longitude_list[1]))
