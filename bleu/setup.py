from setuptools import setup
import sys

try:
    import numpy as np
except ImportError:
    print('First you need to install numpy!', file=sys.stderr)
    sys.exit(1)

try:
    from Cython.Build import cythonize
except ImportError:
    print('First you need to install cython!', file=sys.stderr)
    sys.exit(1)

ext_modules = cythonize('**/*.pyx',
                        language='c++',
                        )

setup(
    name='grasp',
    license='Apache 2.0',
    author='Wilker Aziz',
    author_email='wilkeraziz@gmail.com',
    description='Randomised Semiring Parsing',
    version='0.0.dev1',
    packages=['grasp'],
    include_dirs=[np.get_include()],
    ext_modules=ext_modules,
)
