from setuptools import setup, find_packages

setup(
    name="CustomNVidia",
    version="0.1.0",
    description="Custom NVidia Modules",
    author="Sisung Kim",
    package_dir={"": "stylegan2-ada"},
    packages=find_packages(where="stylegan2-ada"),
    install_requires=[
        "numpy",
        "torch",
    ],
)
