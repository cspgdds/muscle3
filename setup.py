import pathlib
from setuptools import find_packages, setup


_here = pathlib.Path(__file__).resolve().parent
_version_file = _here / 'VERSION'
with _version_file.open('r') as f:
    _version = f.read().strip()

# this is a hack, but it works for now and keeps the version number in a single file
_libmuscle_version_file = _here / 'libmuscle' / 'python' / 'libmuscle' / 'version.py'
with _libmuscle_version_file.open('w') as f:
    f.write('__version__ = \'{}\'\n'.format(_version))

_muscle3_packages = [
        p for p in find_packages() + find_packages('libmuscle/python')
        if p != 'integration_test']

setup(
    name='muscle3',
    version=_version,
    description='Version 3 of the MUltiScale Coupling Library and Environment',
    author='Lourens Veen',
    author_email='l.veen@esciencecenter.nl',
    url='https://github.com/multiscale/muscle3',
    license='Apache License 2.0',
    keywords=['multiscale', 'coupling', 'MUSCLE'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],

    # packages=['muscle_manager', 'muscle_manager_protocol', 'libmuscle', 'libmuscle.mcp'],
    packages=_muscle3_packages,
    package_dir={
        'muscle_manager': 'muscle_manager',
        'libmuscle': 'libmuscle/python/libmuscle'
    },
    entry_points={
        'console_scripts': ['muscle_manager=muscle_manager.muscle_manager:manage_simulation']
    },
    python_requires='>=3.5, <4',
    install_requires=[
        'click',
        'grpcio>=1.24.3, <2',
        'msgpack',
        'netifaces',
        'numpy>=1.12',
        'protobuf>=3.10.0',
        'typing_extensions',
        'ymmsl==0.10.1'          # Also in CI, update there as well
    ],
    setup_requires=[
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'breathe',
        'sphinx',
        'recommonmark',
        'sphinx-rtd-theme'
    ],
    tests_require=[
        'coverage<5',
        'mypy',
        'pytest>=3.5',
        'pytest-cov',
        'pytest-pep8',
        'pytest-flake8',
        'pytest-mypy'
    ],
    extras_require={
        'dev': [
            'grpcio-tools==1.17.1',
            'mypy-protobuf',
            'sphinx',
            'sphinx_rtd_theme',
            'sphinx-fortran',
            'yapf',
            'isort'
        ]
    },
)

# clean up the version file again
_libmuscle_version_file.unlink()
