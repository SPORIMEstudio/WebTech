from setuptools import setup, find_packages

setup(
    name="webtech",
    version="1.0.0",
    author="SPORIMEstudio",
    description="Web Tech - Ethical Web Technology Scanner",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "webtech=webtech.cli:run"
        ]
    },
    python_requires=">=3.7"
)