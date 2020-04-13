from setuptools import setup, find_packages
import macaw


setup(
    name="macaw",
    version=macaw.__version__,
    author="Brayan Castañeda Aquise",
    author_email="cbr4yan@gmail.com",
    packages=find_packages(),
    extras_require={
        "dev": [
            "pytest==5.4.1"
        ]
    }
)
