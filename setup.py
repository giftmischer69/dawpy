from setuptools import setup

setup(
    name="dawpy",
    version="0.1.0",
    description="python digital audio workstation",
    url="http://github.com/giftmischer69/dawpy",
    author="giftmischer69",
    author_email="giftmischer69@protonmail.com",
    license="MIT",
    packages=["dawpy"],
    zip_safe=False,
    install_requires=["typer", "pickledb", "pydantic", "pycco"],
    entry_points={'console_scripts': ['dawpy = dawpy.__main__:main'], },
)
