add_executable(sll-test sll-main.c)

add_library(sll-lib STATIC "${CMAKE_SOURCE_DIR}/lib/sll.c")

include_directories("${CMAKE_SOURCE_DIR}/include/")

target_link_libraries(sll-test sll-lib)