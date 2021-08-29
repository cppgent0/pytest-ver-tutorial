# pytest-ver-tutorial

## To install

* It is good practice to create a python environment for this
  before installation. Use PyCharm to create it, or
  see https://docs.python.org/3/library/venv.html

  Typically, the name of this environent is
  pytest-ver-tutorial/venv

  Make sure it is activated:

```
source  venv/bin/activate
```

* Linux

```
# this will uninstall pytest_ver if necessary
# and re-install pytest_ver
./do_install
```

* TODO Mac: confirm script works correctly
* TODO Windows+MSYS2: confirm script works correctly
* TODO Windows: create a .bat or power_shell

* Check installation:

```
$ pip list

Package    Version
---------- -------
attrs      21.2.0
iniconfig  1.1.1
packaging  21.0
Pillow     8.3.1
pip        21.1.2
pluggy     0.13.1
py         1.10.0
pyparsing  2.4.7
pytest     6.2.4
pytest-ver 0.0.2     # this may be different version
reportlab  3.6.1
setuptools 57.0.0
toml       0.10.2
wheel      0.36.2
```

## To run all tests

* Linux

```
./doit
```

* TODO Mac: confirm script works correctly
* TODO Windows+MSYS2: confirm script works correctly
* TODO Windows: create a .bat or power_shell

## To run only smoketests

* Linux

```
./doit smoketest1
```

* TODO Mac: confirm script works correctly
* TODO Windows+MSYS2: confirm script works correctly
* TODO Windows: create a .bat or power_shell

## To add additional markers

For an example of how to set a marker, see test_ver.py. Only 1
test is currently marked with smoketest1:

```
    # --------------------
    @pytest.mark.smoketest1
    def test_init2(self):
```

* add additional names to pytest.ini

```
markers =
    smoketest1
    smoketest2
```

* add the names to additional pytest testcases as needed

## What is the generated reports and content

There are 4 types of reports and data:

* protocol - holds protocl and steps
* trace - trace matrix from each requirement to one or more
  protocols that tested them
* summary - overall summary data
* other - other files

### Protocol

* protocol.json - holds the protocol and step data generated when
  the tests were run
* tp_results.pdf - contains the protocol report with results in
  PDF format
* tp_results.txt - holds same in information in text format

### Trace

* trace.json - holds the trace information
* trace.pdf - contains the trace matrix report in PDF format
* trace.txt - holds same in information in text format

### Summary

* summary.json - holds the summary data of the requirement ids
  and protocols that they were tested in
* summary.pdf - contains the summary report in PDF format
* summary.txt - holds same in information in text format

### Other

* ut_results.txt - a copy of the stdout.
* TODO replace this with a properly generated log file

