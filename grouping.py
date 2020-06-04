import csv
import random

CSV_NAME = "indiviuals-list.csv"

END_GROUPS = {}
NON_LEADERS = []

THOSE_IN_GROUPS = []

GROUP_MAX = 10
IS_GROUP_FULL = {}
IS_GROUP_FULL_COUNTER = 0

## Open CSV File and add those with a "TRUE" to the newly formed END_GROUPS, and those with a "FALSE" to the NON_LEADERS group
with open(CSV_NAME, "r") as f:
    for line in csv.reader(f, delimiter=","):
        if line[2] == "TRUE":
            END_GROUPS[line[0]] = []
        else:
            NON_LEADERS.append(line)
            IS_GROUP_FULL[line[0]] = False
    f.close()

## While we haven't exhausted the pool of NON_LEADERS and we haven't filled all the groups
while NON_LEADERS != [] and IS_GROUP_FULL_COUNTER < len(END_GROUPS.keys()):

    ## Choose a random index value so that it corresponds to a valid person in the group

    rand_index = random.randrange(0, len(NON_LEADERS))


    ## If a group isn't full, add the randomly selected person to the group, and then remove it from the pool of NON_LEADERS
    for leader in END_GROUPS.keys():
        if len(END_GROUPS[leader]) < GROUP_MAX - 1:
            END_GROUPS[leader].append(NON_LEADERS[rand_index][0])
            THOSE_IN_GROUPS.append(NON_LEADERS[rand_index][0])
            del NON_LEADERS[rand_index]
            break

    ## Check that all groups are not full
    IS_GROUP_FULL_COUNTER = 0
    for leader in END_GROUPS.keys():
        if len(END_GROUPS[leader]) == GROUP_MAX - 1:
            IS_GROUP_FULL_COUNTER += 1

## Print the output, showing who is part of what group
for leader in END_GROUPS.keys():
    # print("Group Leader: {}".format(leader))
    print("{}".format(leader))
    for member in END_GROUPS[leader]:
        # print("\t{}".format(member))
        print("{}".format(member))
    print("")

## If there are people not part of a group, print those
if NON_LEADERS != []:
    # print("Those not in a group:")
    for index, member in enumerate(NON_LEADERS):
        # print("{:>3}- {}".format(index + 1, member[0]))
        print("{}".format(member[0]))
