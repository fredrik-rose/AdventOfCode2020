# Advent of Code 20

Solutions for the advent of code 2020 puzzles, implemented in Python. The
puzzles can be found here: https://adventofcode.com/2020

## Lessons Learned

### Algorithms

Consider which way to "map" things, e.g. in a directed graph. Reversing the directions may be a good idea.

Dynamic programming is an important algorithm.

Complex numbers can be really nice for 2D coordinate systems, especially in cases with simple rotations.

There may be a math trick that makes the problem easy to solve, like modular inverse, greatest common multiple and
the Chinese remainder theorem.

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

## Numpy

May overflow if using too small data types, Python's int will not overflow.

## itertools

May be really useful.
```
def contains_sum_of_two(numbers, target):
    return any(x + y == target for x, y in itertools.combinations(numbers, 2))
```
