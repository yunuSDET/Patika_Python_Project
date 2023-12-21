def flatten(inputList):
    result = []
    for item in inputList:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


input_list = [[1, 'a', ['cat'], 2,['yellow','green',[10,20,30]]], [[[3]], 'dog'], 4, 5]
output_list = flatten(input_list)
print(output_list)
