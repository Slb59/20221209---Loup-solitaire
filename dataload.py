from csv import reader

class DataLoad:
    def __init__(self):
        path = "C:\\Users\\brico\\Documents\\8_Informatique\\2_Loup solitaire\\Tome1\\loup.csv"
        self.rowList = []
        with open(path, 'r') as csvObj:
            csv_reader = reader(csvObj, delimiter=';')
            self.rowList = list(csv_reader)




