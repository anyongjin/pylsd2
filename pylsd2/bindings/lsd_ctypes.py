#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Update	: anyongjin 2021/06/10
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.1

import ctypes
import os
import sys
import random
import numpy as np


def load_library(plat_paths: dict):
    root_dir = os.path.abspath(os.path.dirname(__file__))

    libdir = 'lib'
    plat_key = 'default'
    if sys.platform == 'win32':
        plat_key = 'x64' if sys.maxsize > 2 ** 32 else 'x86'
    elif sys.platform == 'darwin':
        plat_key = 'darwin'
    libnames = plat_paths.get(plat_key)

    while root_dir is not None:
        for libname in libnames:
            try:
                lsdlib = ctypes.cdll[os.path.join(root_dir, libdir, libname)]
                return lsdlib
            except Exception as e:
                pass
        tmp = os.path.dirname(root_dir)
        if tmp == root_dir:
            root_dir = None
        else:
            root_dir = tmp

    # if we didn't find the library so far, try loading without
    # a full path as a last resort
    for libname in libnames:
        try:
            # print "Trying",libname
            lsdlib = ctypes.cdll[libname]
            return lsdlib
        except:
            pass

    return None


lsdlib = load_library({
    'default': ['linux/liblsd.so'],
    'x86': ['win32/x86/lsd.dll', 'win32/x86/liblsd.dll'],
    'x64': ['win32/x64/lsd.dll', 'win32/x64/liblsd.dll'],
    'darwin': ['darwin/liblsd.dylib']
})
if lsdlib is None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')

edlib = load_library({
    'default': ['linux/libEDLines.so'],
    'x86': ['win32/x86/EDLines.dll'],
    'x64': ['win32/x64/EDLines.dll'],
    'darwin': []
})
if edlib is None:
    raise ImportError('Cannot load dynamic library. Did you compile EDLines?')
