from setuptools import setup

setup(
    name='npd_entropy',
    url='https://github.com/afeutrill/NPD-Entropy',
    author='Andrew Feutrill',
    author_email='andrew.feutrill@adelaide.edu.ua',
    packages=['npd_entropy'],
    install_requires=['numpy', 'numba', 'scipy'],
    version='0.1',
    license='MIT',
    description='A Non-Parametric Differential Entropy Rate estimator',
)
