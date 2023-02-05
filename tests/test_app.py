from src.app import index
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)


def test_index():
    assert index() == 'Hello, World!'
print(os.getcwd())