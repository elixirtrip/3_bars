import json
import math
import argparse
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data['features']


def get_biggest_bar(data):
    return max(data, key=lambda x: x['properties']['Attributes']
               ['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['properties']['Attributes']
               ['SeatsCount'])


def get_bar_longitude_latitude(bar):
    return bar['geometry']['coordinates']


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda x:
               math.hypot((get_bar_longitude_latitude(x)[0] - longitude),
                          (get_bar_longitude_latitude(x)[1] - latitude))
               )


def print_formatted_result(masseg, data):
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


if __name__ == '__main__':
    args = get_console_args()
    try:
        data = load_data(args.file_path)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        sys.exit('Файл не найден или данные не в формате JASON')
    except Exception as e:
        sys.exit(e)
    try:
        latitude = float(input('Введите широту Вашего местоположения:\n'))
        longitude = float(input('Введите долготу Вашего местоположения:\n'))
    except ValueError:
        sys.exit('Введено некорректное значение')

    print_formatted_result('Самый большой бар', get_biggest_bar(data))
    print_formatted_result('Самый маленький бар', get_smallest_bar(data))
    print_formatted_result('Самый близкий бар',
                           get_closest_bar(data, longitude, latitude))
