cmake_minimum_required(VERSION 3.10.1)
project(pylsd2)

set(edlines_src_dir "source/edlines")
set(edlines_src "${edlines_src_dir}/edlines.cpp")

set(lsd_dir "source/lsd/")
set(lsd_src "${lsd_dir}/src/lsd.cpp")

include_directories(
  ${edlines_src_dir}
  ${lsd_dir}/include
  )

add_library(EDLines SHARED ${edlines_src})
add_library(lsd SHARED ${lsd_src})


#set(LIBRARY_OUTPUT_PATH ./lib)


set_target_properties(EDLines
  PROPERTIES
  CXX_STANDARD 11
  )
