import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="Cnnclasifier"
Author_USER_NAME="AIwithAj"
SRC_REPO="chicken-diseases-classification"
AUTHOR_EMAIL="dancerworld60@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Cnn App",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{Author_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)