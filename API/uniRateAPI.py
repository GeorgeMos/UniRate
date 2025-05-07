import pandas as pd
from faker import Faker
from random import randint

class uniRateAPI():
    def login():
        pass

    
    def getRandomUsers():
        gen = Faker()
        data = {
            "index" : [],
            "fName" : [],
            "lName" : [],
            "type" : []
        }

        dataFrame = pd.DataFrame(data)

        for i in range(100):
            name = gen.name()
            fName = name.split(" ")[0]
            lName = name.split(" ")[1]
            dataFrame.loc[i] = [i, fName, lName, "student"]
        
        return dataFrame


    def getRandomReviews():
        gen = Faker()
        data = {
            "index" : [],
            "subCode" : [],
            "userCode" : [],
            "review" : []
        }

        dataFrame = pd.DataFrame(data)

        for i in range(100):
            dataFrame.loc[i] = [i, randint(0, 100), randint(0, 100), gen.text()]

        return dataFrame
        