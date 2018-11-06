# coding: utf-8

"""
    LOCKSS Metadata Service REST API

    API of the LOCKSS Metadata REST Service  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lockss-support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "lockss-metadata-python"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="LOCKSS Metadata Service REST API",
    author_email="lockss-support@lockss.org",
    url="https://github.com/lockss/lockss-metadata-python",
    keywords=["Swagger", "LOCKSS Metadata Service REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API of the LOCKSS Metadata REST Service  # noqa: E501
    """
)
