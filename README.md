# PyCoptimizer
This framework is made to offer, to the user, simplicity to choose what flags can be used for optimization in compilation time. It provides to you a list with compilation flags that can be used in compilation to find your goal: maximize ou minimize some of your numbers, like throughput or execution time.The idea started in a project on CERN, where I ran an genetic algorithm with a list of compilation flags to select the flags that improve the throughput of a target code. 

In this framework, you can define your target code to be improved, define what you want improve (maximize throughput, minimize the execution time or minimize memory usage) with what compilation flags (this list can be made by you or you can use the framework default list) and which technique you want to use. You just need to implement an abstract class, defined by the framework and the parameters to be used. 

This document will be upgraded when it's being increased more features.
