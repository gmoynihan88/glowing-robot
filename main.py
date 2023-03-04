import requests
import json

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Making a get request
    response = requests.get('https://api.github.com')

    # print response
    print(response)

    # print json content
    print(json.dumps(response.json(), indent = 6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




