import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="django-editorjs-field",
    version="0.0.3",
    author="Oliver Christen",
    author_email="christen@app-logik.de",
    description="editorjs.io integration as django model/form field",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ochrstn/django-editorjs-field",
    packages=["editorjs_field"],
    include_package_data=True,
    install_requires=['django>=1.8'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 2.2",
        "Environment :: Web Environment",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
