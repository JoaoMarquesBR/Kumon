import json


with open('levels-configs.json','r') as file: 
    data = json.load(file)


def readMultiplicationOptions() :
    for i in data['Multiplication']['Exam']:
        print(i)

def readExamLevel(examLevel):
    return (data['Multiplication']['Exam'][examLevel])

