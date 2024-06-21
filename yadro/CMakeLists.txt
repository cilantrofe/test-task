cmake_minimum_required(VERSION 3.5.0)
project(
    computer_club 
    LANGUAGES CXX
    VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(computer_club main.cpp ${PROJECT_SOURCE_DIR}/src/computer_club.cpp)

target_include_directories(computer_club PRIVATE ${PROJECT_SOURCE_DIR}/include)