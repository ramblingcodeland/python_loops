from distutils.core import setup, Extension

module1 = Extension('loop', sources=['loopmodule.c', ])

setup(
    name='loopmodule',
    version='0.1',
    description='This is a C loop extension',
    ext_modules=[module1, ]
)

