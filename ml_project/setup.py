import setuptools


setuptools.setup(
    name="heart_diseas_classifier",
    version="0.0.1",
    author="Sabyrbayev Azamat",
    description="A heart diseas classifier package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
