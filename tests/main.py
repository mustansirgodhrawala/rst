import pytest
from rst.rst import main

def func_main_test():
	assert main() == "something"
