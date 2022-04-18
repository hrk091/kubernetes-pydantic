# Copyright (c) 2022 Hiroki Okui
# License: MIT

from setuptools import setup, find_packages
import kubernetes_pydantic

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    REQUIRES = f.readlines()

with open("test-requirements.txt") as f:
    TEST_REQUIRES = f.readlines()

setup(
    name="kubernetes_pydantic",
    version=kubernetes_pydantic.__version__,
    description="Kubernetes python client wrapper for better typing leveraging Pydantic",
    author="Hiroki Okui",
    author_email="hiroki.okui@gmail.com",
    license="MIT",
    url="https://github.com/hrk091/kubernetes-pydantic",
    keywords=["Kubernetes", "Pydantic"],
    packages=find_packages(exclude=["kubernetes_pydantic.tests"]),
    install_requires=REQUIRES,
    tests_requires=TEST_REQUIRES,
    include_package_data=True,
    long_description=readme,
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT',
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
