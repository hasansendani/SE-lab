import re


def calculate():
    statement = get_statement()
    validated_statement = validate_statement(statement)
    if not validated_statement:
        return
    for item in validated_statement:
        statement = statement.replace(item, '')
    operations = [char for char in statement]
    priorities = prioritize(operations)
    start_index = 0
    validated_statement = [float(i) for i in validated_statement]

    while 1 in priorities:
        start_index = priorities.index(1)
        validated_statement = operate(validated_statement, operations[start_index], start_index)
        del (priorities[start_index])
        del (operations[start_index])


    while 2 in priorities:
        start_index = priorities.index(2)
        validated_statement = operate(validated_statement, operations[start_index], start_index)
        del (priorities[start_index])
        del (operations[start_index])

    print(validated_statement)
    print("the final result is:")
    print(validated_statement[0])


def operate(nums, operator, start_index):
    if operator == '*':
        nums[start_index] = nums[start_index] * nums[start_index + 1]
        del (nums[start_index + 1])
    elif operator == '/':
        nums[start_index] = nums[start_index] / nums[start_index + 1]
        del (nums[start_index + 1])
    elif operator == '+':
        nums[start_index] = nums[start_index] + nums[start_index + 1]
        del (nums[start_index + 1])
    elif operator == '-':
        nums[start_index] = nums[start_index] - nums[start_index + 1]
        del (nums[start_index + 1])
    return nums


def prioritize(operations):
    priorities = []
    for operation in operations:
        if operation in ["*", "/"]:
            priority = 1
            priorities.append(priority)
            continue
        priority = 2
        priorities.append(priority)
    return priorities


def get_statement():
    print("enter your statement. it should just contain numbers, +, -, *, /")
    statement = input()
    print('your statement is: ' + statement)
    return statement


def validate_statement(statement):
    statement = statement.replace('+', ' ')
    statement = statement.replace('*', ' ')
    statement = statement.replace('/', ' ')
    statement = statement.replace('-', ' ')
    statement = statement.split()
    for item in statement:
        try:
            temp = float(item)
        except:
            print("input is not valid")
            return False
    print("input is valid")
    return [i for i in statement]


if __name__ == '__main__':
    calculate()
