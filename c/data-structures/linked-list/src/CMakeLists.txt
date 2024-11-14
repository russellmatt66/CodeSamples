cmake_minimum_required(VERSION 3.12)
project(linked-list C)

option(ARCH_SLL "Enable build for singly-linked list" OFF)

if (ARCH_SLL)
    add_subdirectory("./driver/" "${CMAKE_SOURCE_DIR}/../build/sll")
endif()