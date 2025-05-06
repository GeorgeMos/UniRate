import pandas as pd
from faker import Faker

#Static class(interface) implementation of the simulated uni api
class upAPI():
    def login():
        pass

    def getRandomSubjects(searchTerm):
        data = {
            "index" : [],
            "name" : []
        }

        dataFrame = pd.DataFrame(data)

        for i in range(100):
            dataFrame.loc[i] = [i, "Subject: " + str(i)]

        dataFrame.set_index("index", inplace=True)

        reDf = dataFrame[dataFrame['name'].str.contains(searchTerm)]

        return reDf