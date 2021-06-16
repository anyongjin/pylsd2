cmake_minimum_required (VERSION 2.8)

project ("EDLines")

INCLUDE_DIRECTORIES(
    .
)

SET(LIBRARY_OUTPUT_PATH ./lib)

add_library(EDLines SHARED
	./edlines.cpp
)
