#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File  : wrapper.py
# Author: anyongjin
# Date  : 2021/6/10
import ctypes
from pylsd2.bindings.fn_types import *


def _build_args(src):
    n_out = c_int()
    rows, cols = src.shape
    src_data = src.flatten().tolist()
    img = (ctypes.c_double * len(src_data))(*src_data)
    return n_out, img, ctypes.c_int(rows), ctypes.c_int(cols)


def _get_lines(return_val, n_out, as_int=True):
    line_dim = 7
    line_len = n_out.value
    lines = [return_val[i * line_dim: (i + 1) * line_dim] for i in range(line_len)]
    if as_int:
        result_lines = []
        for l in lines:
            result_lines.append([round(l[0]), round(l[1]), round(l[2]), round(l[3])] + l[4:])
        lines = result_lines
    CFree_lines(return_val)
    return lines


def LineSegmentDetection(src, blur_scale=0.8, sigma_scale=0.6, quant=2.0, ang_th=22.5,
                         log_eps=0.0, density_th=0.7, n_bins=1024, as_int=True):
    '''
    LSD Full Interface
    :param src: single channel image(e.g. gray img)
    :param blur_scale: When different from 1.0, LSD will scale the input image
                       by 'scale' factor by Gaussian filtering, before detecting
                       line segments.
                       Example: if scale=0.8, the input image will be subsampled
                       to 80% of its size, before the line segment detector
                       is applied.
                       Suggested value: 0.8
    :param sigma_scale: When scale!=1.0, the sigma of the Gaussian filter is:
                       sigma = sigma_scale / scale,   if scale <  1.0
                       sigma = sigma_scale,           if scale >= 1.0
                       Suggested value: 0.6
    :param quant: Bound to the quantization error on the gradient norm.
                   Example: if gray levels are quantized to integer steps,
                   the gradient (computed by finite differences) error
                   due to quantization will be bounded by 2.0, as the
                   worst case is when the error are 1 and -1, that
                   gives an error of 2.0.
                   Suggested value: 2.0
    :param ang_th: Gradient angle tolerance in the region growing
                   algorithm, in degrees.
                   Suggested value: 22.5
    :param log_eps: Detection threshold, accept if -log10(NFA) > log_eps.
                   The larger the value, the more strict the detector is,
                   and will result in less detections.
                   (Note that the 'minus sign' makes that this
                   behavior is opposite to the one of NFA.)
                   The value -log10(NFA) is equivalent but more
                   intuitive than NFA:
                   - -1.0 gives an average of 10 false detections on noise
                   -  0.0 gives an average of 1 false detections on noise
                   -  1.0 gives an average of 0.1 false detections on nose
                   -  2.0 gives an average of 0.01 false detections on noise
                   .
                   Suggested value: 0.0
    :param density_th: Minimal proportion of 'supporting' points in a rectangle.
                       Suggested value: 0.7
    :param n_bins: Number of bins used in the pseudo-ordering of gradient
                   modulus.
                   Suggested value: 1024
    :return:
    '''
    n_out, img, rows, cols = _build_args(src)
    res = CLineSegmentDetection(byref(n_out), img, cols, rows, blur_scale, sigma_scale, quant, ang_th,
                                log_eps, density_th, n_bins, None, None, None)
    return _get_lines(res, n_out, as_int)


def lsd_scale(src, blur_scale=0.8, as_int=True):
    n_out, img, rows, cols = _build_args(src)
    res = CLsd_scale(byref(n_out), img, cols, rows, blur_scale)
    return _get_lines(res, n_out, as_int)


def lsd(src, as_int=True):
    n_out, img, rows, cols = _build_args(src)
    res = CLsd(byref(n_out), img, cols, rows)
    return _get_lines(res, n_out, as_int)


'''
wrappers for ED_lib
'''


def _to_uchar(img_arr):
    src_data = img_arr.flatten().tolist()
    img = (ctypes.c_ubyte * len(src_data))(*src_data)
    return img


def _get_ed_lines(return_val, n_out, as_int=True):
    line_dim = 4
    line_len = n_out.value
    lines = [return_val[i * line_dim: (i + 1) * line_dim] for i in range(line_len)]
    if as_int:
        result_lines = []
        for l in lines:
            result_lines.append([round(l[0]), round(l[1]), round(l[2]), round(l[3])] + l[4:])
        lines = result_lines
    CFreeLinesED(return_val)
    return lines


def LineSegmentDetectionED(img_arr, scaleX=1, scaleY=1, grad_thres=80, anchor_thres=2, scan_interval=2,
                           min_line_len=15, line_fit_err_thres=1.4,
                           gs_ksize=None, gs_sigma=0.6, as_int=True):
    '''
    EDLine Line segment detect method based on EdgeDrawing
    :param img_arr: single channel image
    :param scaleX: downscale factor in X-axis
    :param scaleY: downscale factor in Y-axis
    :param grad_thres: Threshold of gradient image
    :param anchor_thres: Threshold of anchor image
    :param scan_interval: anchor testing can be performed at different scan intervals,
            i.e., every row/column, every second row/column etc. Default value is 2
    :param min_line_len: minimal acceptable length for initial line
    :param line_fit_err_thres: max allow fit error in LeastSquaresLineFit
    :param gs_ksize: ksize for gaussian blur, 2-dim tuple, auto set if not provided
    :param gs_sigma: sigma for gaussian blur, default: 0.6
    :param as_int: round float to int
    :return: [(x1, y1, x2, y2), ...]
    '''
    n_out = c_int()
    rows, cols = img_arr.shape
    gs_kx, gs_ky = 0, 0
    if gs_ksize and len(gs_ksize) == 2:
        gs_kx, gs_ky = gs_ksize
    rsp = CLineSegmentDetectionED(byref(n_out), _to_uchar(img_arr), c_int(cols), c_int(rows),
                                  c_float(scaleX), c_float(scaleY), c_short(grad_thres), c_short(anchor_thres),
                                  c_short(scan_interval), c_int(min_line_len), c_float(line_fit_err_thres),
                                  c_int(gs_kx), c_int(gs_ky), c_float(gs_sigma))
    return _get_ed_lines(rsp, n_out, as_int)

