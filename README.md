# Simple algorithm that given an M X N matrix return all numbers that are the maximum value inits row but the minimum in its column

> **Note:** All the commands are based on a Unix based system such as _OSX_.
> For a different system look for similar commands for it.
> You need an instance of both MySQL and SQL server running.

## Setup

We are using Python version 3.9.7

```bash
$ python --version
Python 3.9.7
```

### Python virtual environment

**Create** a virtual environment:

```bash
$ python3 -m venv .venv
```

`.venv` is the name of the folder that would contain the virtual environment.

**Activate** the virtual environment:

```bash
$ source ./.venv/bin/activate
```

The code should be present in the `simpleAlgorithm.py` file.

**Run the python file** named simpleAlgorithm.py

```bash
$ python -m simpleAlgorithm
```

**Input the matrix's values as prompted** in the format [[1,2,3],[4,5,6],... then clink enter

```bash
$ Enter the matrix in the format [[1,2,3],[4,5,6],...]: [[5,16,20],[9,11,18],[15,16,17]]
```

The value should be printed on the terminal after execution.
