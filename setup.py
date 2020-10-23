# resources:    https://pythonhosted.org/an_example_pypi_project/setuptools.html
#               https://docs.python-guide.org/writing/structure/

from setuptools import setup, find_packages

setup(
    name='PythonClingo_Interface',
    version='1.0.0',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src", exclude=['tests', 'tests.*']),
    package_dir={"": "src"},
    url='https://github.com/BerkWerk/PythonClingo_Interface',
    license='',
    author='Oskar & Berk',
    author_email='',
    description='A library to interface python(especially jupyter notebook) code with clingo',
    # install_requires=['numpy==1.8.1'],  #  package dependencies
    # entry_points={'console_scripts': ['run = mypackage.module1:run']},  # useful if you want to run from terminal/console (functions made available as command-line tools)
    ### automatic versioning
    use_scm_version={
        'write_to': 'version.py',
        'write_to_template': '__version__= "{version}"',
        'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$'
    },
    setup_requires=['setuptools_scm']
)
