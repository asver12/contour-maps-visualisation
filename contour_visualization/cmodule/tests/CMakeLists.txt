set(CMAKE_CXX_FLAGS "-std=c++11 -O3 -Wall -Werror -fopenmp")

include_directories (${TEST_SOURCE_DIR}/src
                   ${PROJECT_SOURCE_DIR}/include
                   ${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR}
                   )


add_executable(runBlendingOperatorsUnitTests blendingOperatorsTests.cpp ${PROJECT_SOURCE_DIR}/src/blendingOperators.cpp)
target_link_libraries(runBlendingOperatorsUnitTests gtest ${CMAKE_THREAD_LIBS_INIT})

add_executable(runPictureMergeUnitTests pictureMergeTests.cpp ${PROJECT_SOURCE_DIR}/src/pictureMerge.cpp ${PROJECT_SOURCE_DIR}/src/blendingOperators.cpp ${PROJECT_SOURCE_DIR}/src/rgb.cpp ${PROJECT_SOURCE_DIR}/src/cieLab.cpp)
target_link_libraries(runPictureMergeUnitTests gtest ${CMAKE_THREAD_LIBS_INIT})

