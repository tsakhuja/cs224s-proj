# Class: CS224S
# Assignment: HW4
# Author: Frank Liu
#
# Formats the training data for use in the classifier.

f_handle = open('feats/features_to_use', 'r')

feature_nums = f_handle.readlines()

f_handle.close()



# open the feature file

f_handle = open('feats/train.lsvm', 'r')

lines = f_handle.readlines()

f_handle.close()



# rewrite the features to the same file (overwrite)
f = open('feats/train_formatted.lsvm', 'w')
for i, line in enumerate(lines):
    if i <= 24: # BRK
        label = 1
    elif i <= 125: # BRM
        label = 2
    elif i <= 2139: # GRW
        label = 3
    elif i <= 2362: # LRM
        label = 4
    elif i <= 2468: # LRR
        label = 5
    elif i <= 2474: # MCR
        label = 6
    elif i <= 2506: # ROR
        label = 7
    elif i <= 2559: # RRM
        label = 8
    elif i <= 2693: # RUM
        label = 9
    elif i <= 2988: # SQK
        label = 10
    elif i <= 3018: # SQL
        label = 11
    elif i <= 3122: # TMP
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

f.close()
