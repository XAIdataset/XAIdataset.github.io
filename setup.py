from setuptools import setup, find_packages

setup(
    name="xaibenchmark",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",  # List your package's dependencies here
        "torch", 
        "torchvision",
        "pandas",
        'Pillow',
    ],
)
