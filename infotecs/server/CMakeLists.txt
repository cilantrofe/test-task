cmake_minimum_required(VERSION 3.10)
project(SereverApp)

set(CMAKE_CXX_STANDARD 11)

set(INCLUDE_DIR
    ${PROJECT_SOURCE_DIR}/include)

set(SOURCES
    main.cpp
    src/server.cpp
)

set(HEADERS
    ${INCLUDE_DIR}/server.hpp
)

add_executable(server ${SOURCES})

target_include_directories(server PRIVATE ${INCLUDE_DIR})
