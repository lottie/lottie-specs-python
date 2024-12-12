import pathlib
from setuptools import setup, find_namespace_packages

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "Readme.md").read_text(encoding="utf-8")

setup(
    name="lottie_specs",
    version="1.0.1",
    description="Tools to load the Lottie standard specs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lottie/lottie-spec-python",
    author="Lottie Animation Community",
    packages=find_namespace_packages(where="src"),
    package_data={"lottie_specs.data": ["*.json"]},
    package_dir={"": "src"},
    python_requires=">=3.10, <4",
    scripts=[
    ],
    project_urls={
        "Bug Reports": "https://github.com/lottie/lottie-spec-python/issues",
        "Source": "https://github.com/lottie/lottie-spec-python",
    },
)
