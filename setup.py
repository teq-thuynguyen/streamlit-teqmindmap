from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-teqmindmap",
    version="0.0.1",
    author="Ember Thuy",
    author_email="thuynguyen@teqnological.asia",
    description="A Streamlit component that enables users to create and interact with mindmaps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[  
        "streamlit >= 0.63",
    ],
)