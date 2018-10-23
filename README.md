# code-examier-p
a bundle of python tools to check code quality

## Tech stack
python3

setupy and pip

## How to run
```
manman$ pip install .
# to have the command line build locally
```
```
manman$ code_exam --file=/Users/manman/PycharmProjects/untitled1/com/path/get_file_info.py --language=.py --dir=/Users/manman/PycharmProjects/untitled1/code_examiner
# all the lines and count......
```

```
Sample output in console

--------------------------
Total Files Number:  2
File details:  [PosixPath('/Users/manman/PycharmProjects/untitled1/code_examiner/get_file_info.py'), PosixPath('/Users/manman/PycharmProjects/untitled1/code_examiner/__init__.py')]
Total lines Before:  133
Filtered lines ( 74% ) :  99
Core logic ( 74% ) :  99
--------------------------
```


