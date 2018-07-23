from setuptools import setup, find_packages

setup(
    name='PyCoptimizer',
    version='0.1',
    description='Python Code Optimization using compilation flags',
    author='Leticia Figueiredo',
    author_email='letfreirefigueiredo@gmail.com',
    packages=find_packages(),
    license='Apache License',
    install_requires=['setuptools', 'numpy', 'matplotlib'],
    package_dir={'COptimizer': './PyCoptimizer/COptimizer',
                 'UserParameters': './PyCoptimizer/UserParameters',
                 'Results': './PyCoptimizer/results',
                 'Comp_clean': './PyCoptimizer/framework/comp_clean',
                 'Island': './PyCoptimizer/framework/island'}
)
