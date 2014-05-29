# Class: CS224S
# Assignment: HW4
# Author: Frank Liu
#
# Formats the test data for use in the classifier.

# open the feature file

f_handle = open('feats/features_to_use', 'r')

feature_nums = f_handle.readlines()

f_handle.close()



f_handle = open('feats/test.lsvm', 'r')

lines = f_handle.readlines()

f_handle.close()



# rewrite the features to the same file (overwrite)

f = open('feats/test_formatted.lsvm', 'w')

for i, line in enumerate(lines):

    if i <= 10: # BRK
        label = 1
    elif i <= 54: # BRM
        label = 2
    elif i <= 941: # GRW
        label = 3
    elif i <= 1014: # LRM
        label = 4
    elif i <= 1060: # LRR
        label = 5
    elif i <= 1063: # MCR
        label = 6
    elif i <= 1078: # ROR
        label = 7
    elif i <= 1105: # RRM
        label = 8
    elif i <= 1163: # RUM
        label = 9
    elif i <= 1290: # SQK
        label = 10
    elif i <= 1303: # SQL
        label = 11
    elif i <= 1348: # TMP
        label = 12

    features = line.split(' ')



    to_write = str(label)

    for feature_num in feature_nums:

      if (len(feature_num.split(':')) == 1):

        to_write += ' ' + features[int(feature_num)]

      else:

        start = feature_num.split(':')[0]

        end = feature_num.split(':')[1]

        for i in range(int(start), int(end)):

          to_write += ' ' + features[i]

    f.write(to_write + '\n')

    # f.write(str(label) + line[1:])



f.close()
