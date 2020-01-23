import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Graphical-Data-Faker",
    version="1.1.0",
    author="Orrin Gradwell",
    author_email="kamakazy000@gmail.com",
    description="a Tool that can spoof personal details for use during development or testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OrrinGradwell/Graphical-Data-Faker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.7',
)