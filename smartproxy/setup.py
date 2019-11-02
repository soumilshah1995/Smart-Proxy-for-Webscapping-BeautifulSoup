from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pyproxywebscrapper",
    version="4.0.0",
    description=""" This Package will be useful for people who are doing webscrapping 
    usually when doing web scrapping if you make to many request 
    the server will block your IP Address
    
    There  is a way to trick the server using Random Ip from different 
    country.Every Request we make we will use unique Ip and Port number 
    check out doccumentation for more details 
         
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/AppleStock",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["smartproxy"],
    include_package_data=True,
    install_requires=["requests"]
)