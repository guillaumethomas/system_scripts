#!/usr/bin/env python3
from os import walk


def read_nas_fs(location):
    ''''
    return a fast list of file
    '''
    movie_ext_set = {'.M4V', '.avi', '.m4v', '.mkv', '.mp4'}
    all_data = list(walk(location))
    tmp_list = list(map(lambda x: x[2], all_data))
    list_file = [j for i in tmp_list for j in i
                 if i != [] and j[-4:] in movie_ext_set]
    return all_data, list_file


if __name__ == '__main__':
    '''

    '''
    locations = {'WS': '/Volumes/Public/Shared Videos',
                 'LG': '/Volumes/service/DLNA'}
    all_data = list()
    list_films = list()
    nas = dict()
    for location in locations.items():
        nas[location[0]] = read_nas_fs(location[1])
        # print(len(list_films[-1]))
    print('{}\n'.format(nas.keys()))
    compare = [i[1] for i in nas.values()]
    for i in compare:
        i.sort()
    not_in = [j for j in compare[1] if j not in compare[0]]
    for i in not_in:
        print(i)
