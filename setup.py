# resources:    https://pythonhosted.org/an_example_pypi_project/setuptools.html
#               https://docs.python-guide.org/writing/structure/

from setuptools import setup, find_packages

setup(
    name='PythonClingo_Interface',
    version='1.0.0',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/BerkWerk/PythonClingo_Interface',
    license='',
    author='Oskar & Berk',
    author_email='',
    description='A library to interface python(especially jupyter notebook) code with clingo',
    # automatic versioning
    use_scm_version=True,
    setup_requires=['setuptools_scm']
)


