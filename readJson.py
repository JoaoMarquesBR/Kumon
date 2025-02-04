import json


with open('levels-configs.json','r') as file: 
    data = json.load(file)


def readMultiplicationExamOptions() :
    return  list(data['Multiplication']['Exam'])
        

def readExamLevel(examLevel):
    return (data['Multiplication']['Exam'][examLevel])

