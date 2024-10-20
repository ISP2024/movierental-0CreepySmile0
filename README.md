## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

- 2.1 Inappropriate Intimacy. `Rental` class use `price_code` from movie class to calculate price and points.
- 2.2 Single Responsibility Principle. `Rental` class is the only class that need `price_code` for calculation, while `Movie` doesn't actually need it.

