#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Update	: anyongjin 2021/06/10
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.2

import os
import pathlib

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig

class CMakeExtension(Extension):
    """From https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py """
    def __init__(self, name):
        super().__init__(name, sources=[])

class build_ext(build_ext_orig):
    """ From https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py """
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        cwd = pathlib.Path().absolute()

        # these dirs will be created in build_py, so if you don't have
        # any python sources to bundle, the dirs will be missing
        build_temp = pathlib.Path(self.build_temp)
        build_temp.mkdir(parents=True, exist_ok=True)
        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        extdir.mkdir(parents=True, exist_ok=True)

        # example of cmake args
        config = 'Debug' if self.debug else 'Release'
        cmake_args = [
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + str(extdir.parent.absolute()),
            '-DCMAKE_BUILD_TYPE=' + config
        ]

        # example of build args
        build_args = [
            '--config', config,
            '--', '-j4'
        ]

        os.chdir(str(build_temp))
        self.spawn(['cmake', str(cwd)] + cmake_args)
        if not self.dry_run:
            self.spawn(['cmake', '--build', '.'] + build_args)
        # Troubleshooting: if fail on line above then delete all possible
        # temporary CMake files including "CMakeCache.txt" in top level dir.
        os.chdir(str(cwd))

setup(
    name='pylsd2',
    version='0.0.3',
    description='pylsd2 is the python bindings for Line Segment Detection(LSD and EDLines)',
    author='Gefu Tang, anyongjin',
    author_email='anyongjin163@163.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/anyongjin/pylsd2',
    ext_modules=[
        CMakeExtension('pylsd2')],
    cmdclass={
        'build_ext': build_ext
        },
    packages=['pylsd2', 'pylsd2.bindings', 'pylsd2.lib'],
    package_dir={'pylsd2.lib': 'pylsd2/lib'},
    package_data={'pylsd2.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
