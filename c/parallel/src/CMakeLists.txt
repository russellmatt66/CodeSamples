cmake_minimum_required(VERSION 3.18)
project(MpiSamples LANGUAGES C)

find_package(MPI REQUIRED)
include_directories(${MPI_INCLUDE_PATH})

# set(FACTPAR_EXEC "factorial/factpar")
# set(FACTSER_EXEC "factorial/factser")
# set(FACTRECUR_EXEC "factorial/factrecur")

add_executable(factpar ../src/factorial/mpi_factorial.c)
add_executable(factser ../src/factorial/ser_factorial.c)
add_executable(factrecur ../src/factorial/ser_factorial_recursive.c)

target_link_libraries(factpar PRIVATE ${MPI_LIBRARIES})
target_link_libraries(factser PRIVATE ${MPI_LIBRARIES})
target_link_libraries(factrecur PRIVATE ${MPI_LIBRARIES})

set_target_properties(factpar PROPERTIES RUNTIME_OUTPUT_DIRECTORY "factorial/")
set_target_properties(factser PROPERTIES RUNTIME_OUTPUT_DIRECTORY "factorial/")
set_target_properties(factrecur PROPERTIES RUNTIME_OUTPUT_DIRECTORY "factorial/")