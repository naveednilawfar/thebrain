import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brain",
    version="1.0",
    author="Naveed Nilawfar",
    author_email="naveednilawfar@gmail.com",
    description="The human brain implemented in python (AI).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naveednilawfar/brain",
    project_urls={
        "Bug Tracker": "https://github.com/naveednilawfar/brain/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
