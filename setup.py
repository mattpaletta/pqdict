from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pqdict",
    version="0.0.1",
    url='https://github.com/mattpaletta/pqdict',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    setup_requires=[],
    author="Matthew Paletta",
    author_email="mattpaletta@gmail.com",
    description="Thread-Safe PQDict Implementation",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license="GNU GPLv3",
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Natural Language :: English",
    ]
)