from setuptools import setup, find_namespace_packages

long_description = None

with open("README", "r") as rtfm:
    long_description = rtfm.read()

setup(
    name="flask_enova",
    version="0.1",
    author="Enova",
    description="simple directory structure for flask projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/tecnologaenova/flask_base_estructure",
    packages=find_namespace_packages(include="flask_enova.*"),
    classifiers=[
        "flask", "Enova", "Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "Flask==1.0", "Flask-Migrate==2.3.0", "Flask-SQLAlchemy==2.3.2"
    ]
)
