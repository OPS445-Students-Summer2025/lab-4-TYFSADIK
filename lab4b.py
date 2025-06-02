#!/usr/bin/env python3


def match_lists(list1, list2):
    return list(set(list1) & set(list2))  # intersection

def diff_lists(list1, list2):
    return list(set(list1) - set(list2))




def match_lists(l1, l2):
    return list(set(l1) & set(l2))

def diff_lists(l1, l2):
    return list(set(l1) ^ set(l2))


def join_lists(list1, list2):
    return list(set(list1) | set(list2))
