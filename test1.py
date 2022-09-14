def my_function(fname):
    print(fname+" Refsnes")

my_function("Emil")
my_function("tobias")
my_function("linus")

import os

source="test3.py"
destination="test2.py"

os.rename(source,destination)