from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='germanium',
    version='1.4.0',
    description='The germanium project: Selenium WebDriver testing API that doesn\'t suck.',
    long_description = readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',

    install_requires=['selenium'],
    packages=['germanium'],
    package_data={'germanium': ['*.js']}
)
