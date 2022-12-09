data = open("data\day6.txt", "r").read()

# print(data)
# data = "bvwbjplbgvbhsrlpgdmjqwftvncz" #test data
#find first non repeating four unique values in a row in the string and return the spot of the last one

def findfirstnonrepeatingfour(data):
    #loop through the string
    for i in range(len(data)-14):
        #check if the next four values are unique
        if(len(set(data[i:i+14])) == 14):
            #if they are return the spot of the last one
            return i+14
    #if there are no four unique values in a row return -1
    return -1

print(findfirstnonrepeatingfour(data))


# go through input and map to object the directory structure and files and their sizes

# Within the terminal output, lines that begin with $ are commands you executed and lines without are output, very much like some modern computers:

# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.

# data = open("data\day7.txt", "r").read()
# startingdirectory= "/"

# data = data.split("\n")

# filesystem = {}
# #add root directory / to filesystem. directories have files and directories as children but files have no children.
# #files have sizes and directories have no sizes
# filesystem[startingdirectory] = {"files": []}
# #add all directories and files to filesystem
# data = [i.split(" ") for i in data]
# index=1
# currentdirectory = startingdirectory
# #make a copy of currentdeirectory to keep track of the path from the root directory to the current directory

# # def find(element, json):
# #     keys = element.split('.')
# #     rv = json
# #     for key in keys:
# #         rv = rv[key]
# #     return rv
# path = [startingdirectory]
# print(path)
# def deref_multi(data, keys):
#     return deref_multi(data[keys[0]], keys[1:]) \
#         if keys else data

# last = deref_multi(filesystem, path)
# print(last)
# for line in data[0:8]:
#     index += 1
#     if line[0] == "$":
#         if line[1] == "cd":
#             if path == "/":
#                 #go to root directory
#                 currentdirectory = path
#                 continue
#             elif path == "..":
#                 currentdirectory = path[-2]

#                 path = path[:-1]
#                 continue
#             else:
#                 #go to directory
#                 # currentdirectory = path[path]
#             # path.append(currentdirectory)
#             #alter current directory based on the argument
#                 continue
#         elif line[1] == "ls":
#             #means list files and directories. we have to add directories and files to the current directory as files
#             for row in data[index-1:index+25]:
#                 def deref_multi(data, keys):
#                     return deref_multi(data[keys[0]], keys[1:]) \
#                         if keys else data

#                 path = deref_multi(filesystem, path)
#                 if row[0] == "dir":
#                     #add directory to current directory
#                     filesystem[path][row[1]] = {"files": []}
#                 elif row[0].isnumeric():
#                     #add file to current directory
#                     currentdirectory["files"].append(row[1])
#                     #add file size to the file
#                     currentdirectory["files"][row[1]]["size"] = row[0]
#                 else:
#                     #exit the current loop
#                     break
#                 print(filesystem) 
             


#             continue
#     #     filesystem[line[1]] = {"children": [], "size": 0}
#     # elif line[0] == "touch":
#     #     filesystem[line[1]] = {"children": [], "size": int(line[2])}
#     # else:
#     #     print("error")
# print (filesystem)