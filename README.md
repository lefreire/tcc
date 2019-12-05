# PyCoptimizer

This framework is made to offer, to the user, simplicity to choose what flags can be used for optimization in compilation time. It provides to you a list with compilation flags that can be used in compilation to find your goal: maximize ou minimize some of your numbers, like throughput or execution time. The idea started in a project on CERN, where I ran a genetic algorithm with a list of compilation flags to select the flags that improve the target code  throughput.

In this framework, you can define your target code to be improved, define what you want improve (maximize throughput, minimize the execution time or minimize memory usage) with what compilation flags (this list can be made by you or you can use the framework default list) and which technique you want to use. You just need to implement an abstract class, defined by the framework and the parameters to be used.

## Installation

### Dependencies

PyCoptimizer requires:

- Python (>= 2.7.10)
- Matplotlib (>= 2.0.2)
- NumPy (>= 1.13.3)
- Pygmo (>= 2.11)

For Pygmo package, you can follow the instructions to install in the official website: [Installation Guide](https://esa.github.io/pagmo2/install.html).

### User installation

If you already have a working installation of numpy, matplotlib and pygmo, the easiest way to install pycoptimizer is using pip
```
pip install PyCoptimizer
```

## How to use

You can see how to use PyCoptimizer into the **examples** folder in any file with **test** in the name.

## Source code

You can check the latest sources with the command:
```
git clone https://github.com/lefreire/tcc.git
```


## Contact

You can contact me for any problem in:

- E-mail: letfreirefigueiredo@gmail.com
