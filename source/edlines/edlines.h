
#ifndef __EDGE_DRAWING_LINE_H_
#define __EDGE_DRAWING_LINE_H_

#include "float.h"
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
//#include "image_defines.h"
#ifdef __cplusplus
extern "C" {
#endif

#ifdef _WIN32
#ifndef EDLIBRARY_EXPORTS
#    define EDLIBRARY_API __declspec(dllexport)
#else
#    define EDLIBRARY_API __declspec(dllimport)
#endif
#else
#  define EDLIBRARY_API
#endif

typedef struct
{
	int x;
	int y;
	int width;
	int height;
}boundingbox_t;


typedef struct
{
	float startx;
	float starty;
	float endx;
	float endy;
}line_float_t;


/*
@function    EdgeDrawingLineDetector
@param       [in]      src:						  image,single channel
@param       [in]      w:                         width of image
@param       [in]      h:                         height of image
@param       [in]      scaleX:                    downscale factor in X-axis
@param       [in]      scaleY:                    downscale factor in Y-axis
@param       [in]      bbox:                      boundingbox to detect
@param       [in/out]  lines:                     result
@return£º										  0:ok; 1:error
@brief£º

*/
EDLIBRARY_API int EdgeDrawingLineDetector(unsigned char* src, int w, int h, float scaleX, float scaleY, boundingbox_t bbox,
	std::vector<line_float_t>& lines, short gradThres = 80,
	short anchorThres = 2, short scanInterval = 2, int minLineLen = 15, float lineFitErrThres = 1.4f,
	int gs_kx = 0, int gs_ky = 0, float gs_sigma = 0.6f);


/*
@function    EdgeDrawingLineDetector
@param       [in]      src:						  image,single channel
@param       [in]      w:                         width of image
@param       [in]      h:                         height of image
@param       [in]      scaleX:                    downscale factor in X-axis
@param       [in]      scaleY:                    downscale factor in Y-axis
@param       [in]      bbox:                      boundingbox to detect
@param       [in/out]  lines:                     result
@return£º										  0:ok; 1:error
@brief£º

*/
EDLIBRARY_API double* EdgeDrawingLineDetectorWrapper(int& n_out, unsigned char* src, int w, int h,
	float scaleX, float scaleY, short gradThres = 80,
	short anchorThres = 2, short scanInterval = 2, int minLineLen = 15, float lineFitErrThres = 1.4f,
	int gs_kx = 0, int gs_ky = 0, float gs_sigma = 0.6f);


EDLIBRARY_API void free_lines(double* rtv);



#ifdef __cplusplus
}
#endif

#endif