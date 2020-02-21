# coding: utf-8

"""
    Pollination Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.2.4
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

with open('README.md') as fh:
    long_description = fh.read()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name="pollination-sdk",
    use_scm_version = True,
    setup_requires=['setuptools_scm'],
    description="Pollination Server",
    author="Pollination Solutions",
    author_email="pollination@solutions.cloud",
    url="https://github.com/pollination/python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "Pollination Server"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent"
    ],
)
