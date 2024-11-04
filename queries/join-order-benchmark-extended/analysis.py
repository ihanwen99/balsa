import os


def distribute_files(source_dir, train_files):
    all_files = [file for file in os.listdir(source_dir) if file.endswith('.sql')]
    print("Total files in source directory: {}".format(len(all_files)))
    print("len(train_files): {}".format(len(train_files)))
    test_files = []

    for file in all_files:
        if file not in train_files:
            test_files.append(file)
    test_files = sorted(test_files)
    print(test_files)
    return f"Files distributed: {len(train_files)} to train, {len(all_files) - len(train_files)} to test."


source_directory = "/users/hanwen/balsa/queries/join-order-benchmark-extended"
source_directory = "/users/hanwen/balsa/queries/join-order-benchmark"
train_files1 = ["{}a.sql".format(i) for i in range(1, 34)]
train_files = train_files1

result = distribute_files(source_directory, train_files)
print(result)
