from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('VERSION', 'r') as f:
    version = f.read().strip()

setup(
    name="data_url",
    version=version,
    author="Ellis Wright",
    author_email="ejw@duck.com",
    description="Easy Data URL management for python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/telday/data_url",
    project_urls={
        "API Documentation": "https://data-url.readthedocs.io/en/latest/#"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=['data_url']),
    python_requires=">=3.5"
)
