pylsd2
=============

### 1. Introduction

pylsd2 is the python bindings for [LSD - Line Segment Detector](http://www.ipol.im/pub/art/2012/gjmr-lsd/).  
pylsd2 is forked from [pylsd](https://github.com/primetang/pylsd), and upgrade lsd from 1.5 to 1.6, thanks primetang

Windows and linux is supported currently, merge request for mac is welcome

### 2. Install

directly through `pip` to install it:
```
[sudo] pip install pylsd2
```

### 3. Usage

We can use the package by using `from pylsd2 import LineSegmentDetection`, and `lines = LineSegmentDetection(src)` is the call format for the `LineSegmentDetection` function, where `src` is a Grayscale Image (`H * W` numpy.array), and the return value `lines` is the Detected Line Segment, `lines` is an array of LSDLine instances, the 7-attributes is:

`x1, y1, x2, y2, width, p, log_nfa`

According to these presentations, we can use it just like the following code ([here is the link](https://github.com/anyongjin/pylsd2/tree/master/example)):

* by using cv2 module

```python
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
```

* by using PIL(Image) module

```python
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
```

The following is the result:

* car.jpg by using cv2 module

![](https://github.com/anyongjin/pylsd2/blob/master/example/car.jpg)

![](https://github.com/anyongjin/pylsd2/blob/master/example/cv2_car.jpg)

* house.png by using PIL(Image) module

![](https://github.com/anyongjin/pylsd2/blob/master/example/house.png)

![](https://github.com/anyongjin/pylsd2/blob/master/example/PIL_house.jpg)

### 4. Compile Library from cpp
** Windows **  
```shell
cd source && mkdir build && cd build
cmake ..
```
open the LSD.sln with Visual Studio, and Build The "ALL_BUILD" Project  
** Linux **  
```shell
cd source && mkdir build_so && cd build_so
cmake ..
cmake --build .
```

