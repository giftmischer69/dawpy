from setuptools import setup

dependencies = [x.strip() for x in open("requirements.txt", "r").readlines()]
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dawpy",
    version="0.1.0",
    description="python digital audio workstation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/giftmischer69/dawpy",
    author="giftmischer69",
    author_email="giftmischer69@protonmail.com",
    license="MIT",
    packages=["dawpy"],
    zip_safe=False,
    install_requires=dependencies,
    entry_points={
        "console_scripts": ["dawpy = dawpy.__main__:main"],
    },
)
