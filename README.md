# Advent of Code 20

Solutions for the advent of code 2020 puzzles, implemented in Python. The
puzzles can be found here: https://adventofcode.com/2020

## Lessons Learned

### Algorithms

Consider which way to "map" things, e.g. in a directed graph. Reversing the directions may be a good idea. An other
idea is to represent a graph as edges containing connected nodes (instead of nodes with connected nodes).
```
graph = {edgeA: [nodeA, nodeB], edgeB: [nodeB]}
graph = {nodeA: [nodeB, nodeC], nodeB: [nodeA], nodeC: [nodeA]}
```

Dynamic programming is an important algorithm.

Complex numbers can be really nice for 2D coordinate systems, especially in cases with simple rotations.

There may be a math trick that makes the problem easy to solve, like modular inverse, greatest common multiple and
the Chinese remainder theorem.

An alternative to create a data structure for multi-dimensional data is to just keep a set of the coordinates. For
example, a 3D cube with two possible values could be represented as a set of coordinates for one of the values.

The Shunting-yard algorithm is nice for parsing and evaluating simple math expressions. Note that it is possible to
adjust the algorithm to also perform the calculations. To do this, each time an operator is popped from the operator
stack, pop two operands from the operand stack and apply the operand to these values. Push the result to the operand
stack. See day 18.

The tools lex/yacc can be nice for "compiler/parsing" problems. A recursive descent parser can also be used.

You don't always have to find a clever math solution like finding an equation or pattern for problems with
many iteration and/or much data. A change of data structure may be enough. For example, iterating ten
million times on one million elements is possible of the operations performed each operation are `O(1)`,
but not if they are `O(N)`.

A linked list and a hash map with references to the nodes in the list may be a useful data structure. Then it is
possible to find and re-arrange elements in `O(1)`. For a list of integers, a really simple implementation is to
use a hash map with keys being the nodes and values being the next node:
```
my_list = list(range(10))
linked_list = {node: next_node for node, next_node in zip(my_list, my_list[1:] + [None])}
```

There are nice coordinate systems to be used for hex grids, see https://www.redblobgames.com/grids/hexagons/

### Python

Create a dict from a list of pairs:
```
>>> dict([['a', 1], ['b', 2]])
{'b': 2, 'a': 1}
```

Parse a binary string to int:
```
int(binary_string, 2)
```

Parameter unpacking:
```
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(*my_list)
```

Create set from list of lists:
```
set().union(*my_list_of_lists)
```

Get (and call) an attribute (e.g a function from an object):
```
getattr(MyClass, 'my_func')(arg)
```

`itertools.chain(*iterables)`: make an iterator that returns elements from the first iterable until it is exhausted,
then proceeds to the next iterable, until all of the iterables are exhausted.
```
>>> list(itertools.chain('ABC', 'DEF'))
['A', 'B', 'C', 'D', 'E', 'F']
```

Be careful with simultaneous updates, Python has support for this. Example of rotation:
```
x, y = x*cos_a - y*sin_a, x*sin_a + y*cos_a
```

Be careful when iterating over sets as the values can come in any order.

Get indexes of the sorted list (argsort):
```
[e[0] for e in sorted(enumerate(my_list), key=lambda x: x[1])]
```

A hack for operator precedence problems is to create a class that overloads operators (e.g. +, - @, ...) and then
search and replace operators with an operator with correct precedence. The overloaded operator makes sure that the
correct operation is performed. Then just simply replace each number with `MyClass(number)` and use the `eval()`
function to compute the result. See day 18 (the hack version).

### Regexp

Extract parts from string, `()` defines a "part":

```
pattern = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
match = pattern.match(password)
match.group(1)
match.group(2)
match.group(3)
match.group(4)
```

It is possible to use named groups (`(?P<name>)`) and `.groupdict()` to convert to a dictionary directly.

Use `re.findall()` to get a list of all matches, works also for group patterns.

Search and replace:
```
re.sub(r'(\d+)', r'MyClass(\1)', string)
```

The Python documentation has a nice tokenizer example:
https://docs.python.org/3/library/re.html#writing-a-tokenizer

Regexp does not have support for patterns like `a+b+` where the numbers of `a`s and `b`s must match.

## Numpy

May overflow if using too small data types, Python's int will not overflow.

## itertools

May be really useful.
```
def contains_sum_of_two(numbers, target):
    return any(x + y == target for x, y in itertools.combinations(numbers, 2))
```
