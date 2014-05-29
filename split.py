import os
import shutil
import random

data_dir = "data/data"
test_dir = "data/test"
train_dir = "data/train"
for root__, dirs, files__ in os.walk("data/data"):
    class_name = os.path.basename(root__)
    print (class_name)
    test_class_path = os.path.join(test_dir, class_name)
    train_class_path = os.path.join(train_dir, class_name)
    if not os.path.exists(test_class_path):
        os.makedirs(test_class_path)
    if not os.path.exists(train_class_path):
        os.makedirs(train_class_path)
    file_count = len(files__)
    num_training = int(0.7 * file_count)
    print (class_name, file_count, num_training)
    num_selected = 0
    random.shuffle(files__)
    for the_file in files__:
        file_path = os.path.join(root__, the_file)
        if (num_selected < num_training):
            num_selected += 1
            shutil.copy(file_path, os.path.join(train_class_path, the_file))
        else:
            shutil.copy(file_path, os.path.join(test_class_path, the_file))

