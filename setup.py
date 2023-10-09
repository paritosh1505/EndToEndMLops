import setuptools

with open("README.md","r",encoding="utf-8") as f:
    desc= f.read()

__version__ ="0.0.0"

REP_NAME = "ENDTOENDMLOPS"
AUTHOR_USER_NAME ="paritosh1505"
SRC_REPO="MLOPS_project"
AUTHOR_EMAIL= "rikkiparitosh43@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A setup file",
    long_description=desc,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REP_NAME}",
    project_url={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REP_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
    )