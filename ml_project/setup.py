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
    install_requires=[
            'hydra-core==1.0.6',
            'omegaconf==2.0.6',
            'pandas==1.2.1',
            'pandas-profiling==2.12.0',
            'PyYAML==5.4.1',
            'scikit-learn==0.23.2',
            'numpy==1.19.2',
            'pytest==6.1.1'
    ]
)
