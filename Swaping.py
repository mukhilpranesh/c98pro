def swapFileData(file1, file2):
    with open(file1, 'r') as file:
        data_a = file.read()

    with open(file2, 'r') as file:
        data_b = file.read()

    with open(file1, 'w') as file:
        file.write(data_b)

    with open(file2, 'w') as file:
        file.write(data_a)

file1_name = input("Enter the name of the first file to swap: ")
file2_name = input("Enter the name of the second file to swap: ")

swapFileData(file1_name, file2_name)

print(file1_name+" "+ file2_name +" Swapped succesfully")