from distutils.core import setup

exec(open("./version.py").read())

setup(
    # Application name:
    name="flask-rest",

    # Version number (initial):
    # version="1.0.0",

    # Application author details:
    author="Yevhen Stolietnii",
    author_email="name@addr.ess",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    # Dependent packages (distributions)
    install_requires=[
        "flask-restful",
    ],
)