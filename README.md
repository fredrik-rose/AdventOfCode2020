# Advent of Code 20

Solutions for the advent of code 2020 puzzles, implemented in Python. The
puzzles can be found here: https://adventofcode.com/2020

## Lessons Learned

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
