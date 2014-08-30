cmake_minimum_required(VERSION 2.8)
PROJECT(HelloWorld CXX C)

SET(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

INCLUDE(cmake/FabricEngineModule.cmake)

SET(MODULE_LIBRARIES "")

extension_define("HelloWorld" "src/HelloWorld.fpm.json")
extension_sources(CPP "src/HelloWorld.cpp" KL "src/HelloWorld.kl")
extension_build(${MODULE_LIBRARIES})
