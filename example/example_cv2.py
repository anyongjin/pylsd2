#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Update	: anyongjin 2021/06/10
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.1

import cv2
import numpy as np
import os
from pylsd2 import LineSegmentDetection
fullName = 'car.jpg'
folder, imgName = os.path.split(fullName)
src = cv2.imread(fullName, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
lines = LineSegmentDetection(gray)
for l in lines:
    pt1 = (int(l.x1), int(l.y1))
    pt2 = (int(l.x2), int(l.y2))
    width = l.width
    cv2.line(src, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
cv2.imwrite(os.path.join(folder, 'cv2_' + imgName.split('.')[0] + '.jpg'), src)
