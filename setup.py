import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tello",
    version="0.0.1",
    author="Justin Ruan",
    author_email="justin900429@gmail.com",
    description="Python package for tello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Justin900429/tello",
    packages=["tello"],
    install_requires=[
        "numpy",
        "opencv_python",
    ],
    python_requires=">=3.8"
)
