import os
import re


def remove_idea(root):
    pathDir = os.listdir(root)
    for path in pathDir:
        filepath = os.path.join(root, path)
        if os.path.isdir(filepath):
            remove_idea(filepath)
        elif re.match("^workspace", path):
            print(path)
            os.remove(filepath)


remove_idea("D:\workspace\wisteria\.idea\modules")
