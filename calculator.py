import re

def calculate():
    statement = get_statement()
    validated_statement = validate_statement(statement)
    if not validated_statement:
        return
    operations = []
    for item in validated_statement:
        statement = statement.replace(item, '')
    operations = [char for char in statement]
    priorities = prioritize(operations)
    print(priorities)



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
