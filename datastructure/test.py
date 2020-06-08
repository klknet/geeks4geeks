import os
import re
from linkedlist.base_linked_list import _Node

def remove_idea(root):
    pathDir = os.listdir(root)
    for path in pathDir:
        filepath = os.path.join(root, path)
        if os.path.isdir(filepath):
            remove_idea(filepath)
        elif re.match("^workspace", path):
            print(path)
            os.remove(filepath)


# remove_idea("D:\workspace\wisteria\.idea\modules")
n = _Node()
n.add_all([1,2,3])
n.traverse()
