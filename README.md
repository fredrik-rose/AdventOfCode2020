# Advent of Code 20

Solutions for the advent of code 2020 puzzles, implemented in Python. The
puzzles can be found here: https://adventofcode.com/2020

## Lessons Learned

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

`itertools.chain(*iterables)`: make an iterator that returns elements from the first iterable until it is exhausted,
then proceeds to the next iterable, until all of the iterables are exhausted.
```
>>> list(itertools.chain('ABC', 'DEF'))
['A', 'B', 'C', 'D', 'E', 'F']
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

## Numpy

May overflow if using too small data types, Python's int will not overflow.
