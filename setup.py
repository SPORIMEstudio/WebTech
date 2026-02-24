from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8")as f:
    long_description = f.read()
setup(
    name="sporime-webtech",
    version="1.0.3",
    author="SPORIMEstudio",
    description="Web Tech - Ethical Web Technology Scanner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SPORIMEstudio/WebTech",
    packages=["webtech"],
    include_package_data=True,
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
