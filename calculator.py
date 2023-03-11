import re

def calculate():
    statement = get_statement()
    if not validate_statement(statement):
        return




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
        if not item.isnumeric():
            print(statement)
            print("input is not valid")
            return False
    print("input is valid")
    return [float(i) for i in statement]




if __name__ == '__main__':
    calculate()
