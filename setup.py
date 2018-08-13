from setuptools import setup

setup(
    name='reprexpy',
    version='0.1.0dev',
    description='Render reproducible examples of code (port of R package `reprex`)',
    long_description='See https://github.com/crew102/reprexpy for details',
    author='Christopher Baker',
    author_email='chriscrewbaker@gmail.com',
    url='https://github.com/crew102/reprexpy/issues',
    license='LICENSE.txt',
    classifiers=[],
    packages=['reprexpy'],
    install_requires=[
        'pyperclip',
        'asttokens',
        'nbconvert',
        'nbformat',
        'matplotlib',
        'IPython',
        'pyimgur',
        'setuptools',
        'stdlib-list',
        'jupyter'
    ],
    tests_require=['pytest', 'terminado', 'pyzmq', 'pickledb'],
    setup_requires=["pytest-runner"]
)
