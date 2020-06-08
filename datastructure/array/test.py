import sys
sys.path.append("d:/workspace/GEEKS4GEEKS")
print(sys.path)
from datastructure.linkedlist.base_linked_list import _Node


n = _Node()
n.add_all([1,2,3])
n.traverse()