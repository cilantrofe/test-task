cmake_minimum_required(VERSION 3.10)
project(ClientApp)

set(CMAKE_CXX_STANDARD 11)

set(INCLUDE_DIR
    ${PROJECT_SOURCE_DIR}/include)

set(SOURCES
    main.cpp
    src/client.cpp
)

set(HEADERS
    ${INCLUDE_DIR}/client.hpp
)

add_executable(client ${SOURCES})

target_include_directories(client PRIVATE ${INCLUDE_DIR})
