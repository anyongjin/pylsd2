#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021/06/10
# @Author  : anyongjin (anyongjin163@163.com)
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.1
from ctypes import *
from pylsd2.bindings.lsd_ctypes import lsdlib


class LSDLine:
    def __init__(self, line_arr):
        self.x1 = line_arr[0]
        self.y1 = line_arr[1]
        self.x2 = line_arr[2]
        self.y2 = line_arr[3]
        self.width = line_arr[4]
        self.p = line_arr[5]
        self.log_nfa = line_arr[6]

    def __str__(self):
        return f'({self.x1},{self.y1})->({self.x2},{self.y2}) width:{self.width}, p:{self.p}, nfa:{self.log_nfa}'


CLineSegmentDetection = lsdlib.LineSegmentDetection
CLineSegmentDetection.restype = POINTER(c_double)
CLineSegmentDetection.argtypes = [
    POINTER(c_int),
    POINTER(c_double),
    c_int,
    c_int,
    c_double,
    c_double,
    c_double,
    c_double,
    c_double,
    c_double,
    c_int,
    POINTER(POINTER(c_int)),
    POINTER(c_int),
    POINTER(c_int),
]

CLsd_scale_region = lsdlib.lsd_scale_region
CLsd_scale_region.restype = POINTER(c_double)
CLsd_scale_region.argtypes = [
    POINTER(c_int),
    POINTER(c_double),
    c_int,
    c_int,
    c_double,
    POINTER(POINTER(c_int)),
    POINTER(c_int),
    POINTER(c_int),
]

CLsd_scale = lsdlib.lsd_scale
CLsd_scale.restype = POINTER(c_double)
CLsd_scale.argtypes = [
    POINTER(c_int),
    POINTER(c_double),
    c_int,
    c_int,
    c_double
]

CLsd = lsdlib.lsd
CLsd.restype = POINTER(c_double)
CLsd.argtypes = [
    POINTER(c_int),
    POINTER(c_double),
    c_int,
    c_int,
]

CFree_lines = lsdlib.free_lines
CFree_lines.restype = None
CFree_lines.argtypes = [POINTER(c_double)]
