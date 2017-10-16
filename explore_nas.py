#!/usr/bin/env python3
from os import walk


def read_nas_fs(location):
    ''''
    return a fast list of file
    '''
    movie_ext_set = {'.M4V', '.avi', '.m4v', '.mkv', '.mp4'}

    tmp_list = list(map(lambda x: x[2], walk(location)))
    list_file = [j for i in tmp_list for j in i if i != []]
    # extension = set([i[-4:] for i in list_file])
    list_file = [i for i in list_file if i[-4:] in movie_ext_set]
    return list_file


if __name__ == '__main__':
    '''

    '''
    locations = ['/Volumes/Public/Shared Videos', '/Volumes/service/DLNA']

    for location in locations:
        list_films = read_nas_fs(location)
        # print(list_films)
        print(len(list_films))
        # print(extension)
