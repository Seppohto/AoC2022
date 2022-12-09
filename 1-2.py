# Get data from txt file data\day1task1.txt
# and save it to variable,
data = open("data\day1.txt", "r").read()
# Then split the data into a dictionary using empty lines as separators
data = data.split("\n\n")
#then split each group into a list of integer answers separated by new lines
datagroup = [group.split("\n") for group in data]
# then transform all values into integers
datagroup = [[int(i) for i in group] for group in datagroup]
# then sum the total of each group and save it to a list
data = [sum(group) for group in datagroup]
# print(data)
# # then check the index of the group that has the highest sum
print(data.index(max(data)) + 1, max(data))
# find out top 3 groups with highest sum and their sum
top3 = sorted(data, reverse=True)[:3]
print(top3)
print(sum(top3))