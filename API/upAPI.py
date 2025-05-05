import pandas as pd


#Static class(interface) implementation of the simulated uni api
class upAPI():
    def login():
        pass

    def getRandomSubjects():
        data = {
            "index" : [0, 1, 2, 3, 4, 5, 6, 7],
            "name" : ["A", "B", "C", "D", "AA", "AB", "AC", "AD"]
        }

        dataFrame = pd.DataFrame(data)
        dataFrame.set_index("index", inplace=True)

        return dataFrame