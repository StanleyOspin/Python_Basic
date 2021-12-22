import zipfile
import os
import collections


def unzip(archive):
    file_zip = zipfile.ZipFile(file_name, 'r')

    for i_file_name in file_zip.namelist():
        file_zip.extract(i_file_name)
    file_zip.close()


def collect_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
    file_name = ''.join((file_name[:-3], 'txt'))
    text = open(file_name, 'r', encoding='utf-8')
    for i_line in text:
        for j_symbol in i_line:
            if j_symbol.isalpha():
                if j_symbol not in result:
                    result[j_symbol] = 0
                result[j_symbol] += 1

    text.close()
    return result


def print_stats(statistic):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))
    for key, value in statistic.items():
        print('|{: ^9}|{: ^9}|'.format(key, value))
    print('+{:-^19}+'.format('+'))


def sorting_by_frequency(statistic_dict):
    sorted_values = sorted(statistic_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in statistic_dict.keys():
            if statistic_dict[j_key] == i_value:
                sorted_dict[j_key] = statistic_dict[j_key]
    return sorted_dict


file_name = os.path.abspath('voyna-i-mir.zip')
statistic = collect_stats(file_name)
statistic = sorting_by_frequency(statistic)
print_stats(statistic)
