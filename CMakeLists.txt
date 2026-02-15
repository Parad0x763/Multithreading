cmake_minimum_required( VERSION 3.15 )
project( multithreading )

set( CMAKE_EXPORT_COMPILE_COMMANDS ON )
set( CMAKE_BUILD_TYPE Debug )
set( CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g" )

set(
    sources
    src/main.cpp
)

find_package( Catch2 REQUIRED )

target_link_libraries( main Catch2::Catch2WithMain )

add_executable( main ${sources} )
