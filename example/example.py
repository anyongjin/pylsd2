#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File  : example.py
# Author: anyongjin
# Date  : 2021/6/16

import os
import numpy as np
from pylsd2 import LineSegmentDetection, LineSegmentDetectionED


def extract_lines(gray, extract_type='lsd'):
    if extract_type == 'lsd':
        lines = LineSegmentDetection(gray)
    else:
        lines = LineSegmentDetectionED(gray)
    return lines


def get_out_path(in_path, extract_type):
    dirname, fname = os.path.split(in_path)
    base_name, ext = os.path.splitext(fname)
    out_dir = os.path.join(dirname, 'out')
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    return os.path.join(out_dir, base_name + '_' + extract_type + ext)


def detect_lines_with_cv2(path, extract_type='lsd'):
    import cv2
    out_path = get_out_path(path, extract_type)
    src = cv2.imread(path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    lines = extract_lines(gray, extract_type)
    for l in lines:
        pt1, pt2 = tuple(l[:2]), tuple(l[2:4])
        cv2.line(src, pt1, pt2, (0, 255, 0), 1)
    cv2.imwrite(out_path, src)


def detect_lines_with_PIL(path, extract_type='lsd'):
    from PIL import Image, ImageDraw
    out_path = get_out_path(path, extract_type)
    img = Image.open(path)
    gray = np.asarray(img.convert('L'))
    lines = extract_lines(gray, extract_type)
    draw = ImageDraw.Draw(img)
    for l in lines:
        pt1, pt2 = l[:2], l[2:4]
        draw.line((pt1, pt2), fill=(0, 0, 255), width=1)
    img.save(out_path)


if __name__ == '__main__':
    img_dir = '.'
    img_exts = {'.jpg', '.png'}
    names = os.listdir(img_dir)
    full_paths = [os.path.join(img_dir, n) for n in names if os.path.splitext(n)[-1] in img_exts]
    for path in full_paths:
        detect_lines_with_cv2(path, 'lsd')
        detect_lines_with_cv2(path, 'edlines')
    print('complete')
