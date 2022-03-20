import os
from urllib import parse

HEADER="""# 
# 제목을 쓰자
# Readme.md 자동 추가
---
"""


def main():
    content = ""
    content += HEADER
    
    directories = [];

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images' or category == 'files':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            if len(files) == 1:
                content += "### [{}]({})\n".format(category, parse.quote(os.path.join(root, files[0])))
                directories.append(category)
            continue
            
        if directory not in directories:
            content += "### {}\n".format(directory)
            directories.append(directory)

        for file in files:
            content += "- [{}]({})\n".format(category, parse.quote(os.path.join(root, file)))
        content += "\n"

    with open("README.md", "w", encoding="UTF-8") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()