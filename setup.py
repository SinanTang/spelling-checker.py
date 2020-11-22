import os
from setuptools import setup, find_packages

# https://packaging.python.org/en/latest/single_source_version.html
version = exec(open("utils/version.py").read())

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="spellcheck",
    version=__version__,
    author="stang",
    author_email="",
    description="A simple spelling checker for English written text",
    license="MIT",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/SinanTang/spelling-checker.py",
    include_package_data=True,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.8',
)
