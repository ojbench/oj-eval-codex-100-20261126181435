cmake_minimum_required(VERSION 3.16)
project(perfect_numbers LANGUAGES CXX)

add_executable(code main.cpp)
target_compile_features(code PRIVATE cxx_std_17)
target_compile_options(code PRIVATE -O2 -Wall -Wextra -Wpedantic)
