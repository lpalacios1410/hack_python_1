"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    new_result = []
    index = 0
    
    while index < len(result):
        new_result.append(result[index])
        if index != len(result) - 1:
            new_result.append('@')
            index+= 1
    # print (new_result)
    return new_result