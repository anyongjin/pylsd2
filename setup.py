#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Update	: anyongjin 2021/06/10
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.2

from setuptools import setup

setup(
    name='pylsd2',
    version='0.0.3',
    description='pylsd2 is the python bindings for Line Segment Detection(LSD and EDLines)',
    author='Gefu Tang, anyongjin',
    author_email='anyongjin163@163.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/anyongjin/pylsd2',
    packages=['pylsd2', 'pylsd2.bindings', 'pylsd2.lib'],
    package_dir={'pylsd2.lib': 'pylsd2/lib'},
    package_data={'pylsd2.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
