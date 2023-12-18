from setuptools import setup, find_packages

setup(
    name="CustomNVidia",
    version="0.1.0",
    description="Custom NVidia Modules",
    author="Sisung Kim",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        "torch",
    ],
)
