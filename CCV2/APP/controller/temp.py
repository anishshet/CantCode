import json
import sys
def add():
    val_array = json.loads(sys.argv[1])
    print(val_array[0]+val_array[1])
    return val_array[0]+val_array[1]

add()