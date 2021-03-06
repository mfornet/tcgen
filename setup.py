import setuptools
from tcgen._version import VERSION

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='tcgen',
    version=VERSION,
    author='Marcelo Fornet',
    author_email='mfornet94@gmail.com',
    description='Program synthesis tool. Read a list of strings and create a generator that sample strings from the same distribution as input strings. Focused on test cases of competitive programming problems.',
    long_description=long_description,
    keywords='program synthesis competitive programming acm icpc codeforces',
    include_package_data=True,
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/mfornet/tcgen',
)
