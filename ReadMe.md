# Multithreading

## Conan

- [Conan](https://conan.io/)
- [Conan-Docs](https://docs.conan.io/2)
- [Simple-Cmake-Project](https://docs.conan.io/2/tutorial/consuming_packages/build_simple_cmake_project.html)
- [conanfile.py](https://docs.conan.io/2/reference/conanfile.html)
- `conan install . -sbuild_type=Debug -of=conan/deb --build=missing`
- Add the following the the `conanfile.py` for configuring the bulild settings and generators
```
generators = ( "CMakeToolchain", "CMakeDeps" )
settings = ( "os", "build_type", "arch", "compiler" )
```
