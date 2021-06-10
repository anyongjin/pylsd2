#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Update	: anyongjin 2021/06/10
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.1

from PIL import Image, ImageDraw
import numpy as np
import os
from pylsd2 import LineSegmentDetection
fullName = 'house.png'
folder, imgName = os.path.split(fullName)
img = Image.open(fullName)
gray = np.asarray(img.convert('L'))
lines = LineSegmentDetection(gray)
draw = ImageDraw.Draw(img)
for l in lines:
    pt1 = (int(l.x1), int(l.y1))
    pt2 = (int(l.x2), int(l.y2))
    width = l.width
    draw.line((pt1, pt2), fill=(0, 0, 255), width=int(np.ceil(width / 2)))
img.save(os.path.join(folder, 'PIL_' + imgName.split('.')[0] + '.jpg'))
