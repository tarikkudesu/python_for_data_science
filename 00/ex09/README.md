# ft_package

A simple Python package that provides a utility function to count how many times a string occurs in a list.

## Installation

You can install this package using the source code locally:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Or:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

Import the function directly from the package:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## Function

### `count_in_list(totos, toto)`

Counts how many times `toto` occurs in the list `totos`.

**Parameters:**
- `totos` (list): The list to search through.
- `toto` (string): The string to count.

**Returns:**
- `int`: The number of occurrences of `toto` in `totos`.

## License

MIT