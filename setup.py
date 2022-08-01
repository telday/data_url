from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="data_url",
    version="1.0.5",
    author="Ellis Wright",
    author_email="ejw393@duck.com",
    description="",
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
