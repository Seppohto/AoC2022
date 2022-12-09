# (your puzzle input). For example:

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
# Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
# Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

# The total sizes of the directories above can be found as follows:

# The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
# The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
# Directory d has total size 24933642.
# As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?


data = open('data/day7.txt').read().splitlines()
filesystem = {}
filesystem["/"] = {}
path = ["/"]

def find(path, json):
    keys = path
    rv = json
    for key in keys:
        rv = rv[key]
    return rv

for line in data[1:len(data)]:
    store = find(path, filesystem)
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                #remove last directory from path
                path=path[:-1]
                pass
            else:
                #move to directory
                path.append(line[2])
        elif line[1] == 'ls':
            #list contents of current directory
            pass
    elif line[0] == 'dir':
        store[line[1]]={}
    else:
        store[line[1]] = {'type': 'file', 'size': int(line[0])}

# calculate total size of each directory
def calculate_size(json):
    if 'type' in json:
        return json['size']
    else:
        size = 0
        for key in json:
            size += calculate_size(json[key])
        return size

path = ["/"]
small_directories = []
all_directory_sizes = []
store = find(path, filesystem)
store['total_size'] = calculate_size(store)
for line in data[1:len(data)]:
    store = find(path, filesystem)
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                #remove last directory from path
                path=path[:-1]
                pass
            else:
                #move to directory
                path.append(line[2])
        elif line[1] == 'ls':
            pass
    elif line[0] == 'dir':
        store[line[1]]['total_size'] = calculate_size(store[line[1]])
        # add path and size to all_directory_sizes
        all_directory_sizes.append({'path': path + [line[1]], 'size': store[line[1]]['total_size']})
        #if size is <= 100000, add path and size to small_directories
        if store[line[1]]['total_size'] <= 100000:
            small_directories.append({'path': path + [line[1]], 'size': store[line[1]]['total_size']})

    else:
        pass



# calculate sum of total sizes of small directories
sum = 0
for directory in small_directories:
    sum += directory['size']

print(sum)


# --- Part Two ---
# Now, you're ready to choose a directory to delete.

# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

# To achieve this, you have the following options:

# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

#get the directory size of / (root)
print(filesystem['/']['total_size'])

# calculate the size of unused space
unused_space = 70000000 - filesystem['/']['total_size']
print(unused_space)
#find the smallest directore that would free up enough space
smallest_directory = {'path': [], 'size': 279196526}
for directory in all_directory_sizes:
    if directory['size'] >= 30000000-unused_space:
        if directory['size'] < smallest_directory['size']:
            smallest_directory = directory

print(smallest_directory)