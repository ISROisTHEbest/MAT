import json

#Local Functions
def genid():
    try:
        with open('questions.json') as file:
            data = json.load(file)
            data2 = []
            for i in data.keys():
                data2.append(i)
            data = data2[-1]
            data = int(data) + 1
            return data
    except:
        return 1

    
#Main Functions   
def gethintf(q):
    with open('questions.json') as file:
        data = json.load(file)
    try:
        return data[q]["hint"]
    except:
        return None
    
 
def getansf(q):
    with open('questions.json') as file:
        data = json.load(file)
    try:
        return data[q]["answer"]
    except:
        return None
    
def qdumpf(q,ans,hint):
    for i in q:
        if str(i).isupper():
            q = str(q).replace(i, f' {i}')
    try:
        with open('questions.json') as file:
            data = json.load(file)
            data[str(genid())] = {"question":q, "answer":ans, "hint":hint}
        with open('questions.json', 'w') as file: 
            json.dump(data, file)
        return {"status":"true"}
    except Exception as e:
        return {"status":e}

def getqf(qid):
    with open('questions.json') as file:
        data = json.load(file)
    try:
        return data[qid]["question"]
    except:
        return None

    

    