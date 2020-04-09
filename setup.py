from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyCoptimizer',
    version='0.1.1',
    description='Python Code Optimization using compilation flags',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Leticia Figueiredo',
    author_email='letfreirefigueiredo@gmail.com',
    packages=find_packages(),
    license='Apache License',
    install_requires=['setuptools', 'numpy', 'matplotlib'],
    package_dir={'COptimizer': './PyCoptimizer/coptimizer',
                 'UserParameters': './PyCoptimizer/user_parameters',
                 'Results': './PyCoptimizer/results',
                 'CompClean': './PyCoptimizer/framework/comp_clean',
                 'Island': './PyCoptimizer/framework/island'}
)
