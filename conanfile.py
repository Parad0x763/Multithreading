from conan import ConanFile
from conan.tools.cmake import cmake_layout

class Multithreading( ConanFile ):
    name = "multithreading"
    description = "This is a simple project exploring multithreading in C++"
    generators = ( "CMakeToolchain", "CMakeDeps" )
    settings = ( "os", "build_type", "arch", "compiler" )

    """Packages that are required for the project"""
    def requirements( self ):
        self.requires( "catch2/3.12.0" )

    def layout( self ):
        cmake_layout( self )