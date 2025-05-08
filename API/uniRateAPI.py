import pandas as pd
from faker import Faker
from random import randint

def genRevData():
        gen = Faker()
        data = {
            "index" : [],
            "subCode" : [],
            "userCode" : [],
            "review" : []
        }

        dataFrame = pd.DataFrame(data)

        for i in range(1000):
            dataFrame.loc[i] = [i, randint(0, 100), randint(0, 100), gen.text()]
        dataFrame.set_index("index", inplace=True)
        return dataFrame



def genUserData():
    gen = Faker()
    data = {
        "index" : [],
        "code"  : [],
        "fName" : [],
        "lName" : [],
        "type" : []
    }

    dataFrame = pd.DataFrame(data)
    for i in range(100):
        name = gen.name()
        fName = name.split(" ")[0]
        lName = name.split(" ")[1]
        dataFrame.loc[i] = [i, i, fName, lName, "student"]
    dataFrame.set_index("index", inplace=True)
        
    return dataFrame


revData = genRevData()
userData = genUserData()
class uniRateAPI():
    def login():
        pass

    def getRandomUsers(code):
        reDf = userData[userData['code'] == code]
        return reDf


    def getRandomReviews(subCode :int):
        reDf = revData[revData['subCode'] == subCode]
        return reDf
        