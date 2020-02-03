import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rhutils", 
    version="0.0.2",
    author="altctrlmm",
    author_email="micahmrocks@gmail.com",
    description="Robinhood Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/altctrlmm/rhutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)