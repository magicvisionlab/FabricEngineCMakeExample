PROJECT(HelloWorld CXX C)

SET(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

INCLUDE(cmake/FabricEngineModule.cmake)

SET(MODULE_SPEC "src/HelloWorld.fpm.json")
SET(MODULE_CPP_SOURCES "src/HelloWorld.cpp")
SET(MODULE_KL_SOURCES "src/HelloWorld.kl")

add_fabricengine_extension("HelloWorld")
