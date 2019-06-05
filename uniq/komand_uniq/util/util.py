import komand
import json


def element_count(orig_ls):
    '''Count frequency of each element in array'''
    d={}
    dups = d.fromkeys(orig_ls, 0)
    for i in orig_ls:
        dups[i] += 1
    return dups

def duplicate_count(orig_ls, new_ls):
    '''Count total number of duplicates'''
    orig_count = len(orig_ls)
    new_count = len(new_ls)
    count = orig_count - new_count
    return count
