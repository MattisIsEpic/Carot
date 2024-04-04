import socket
import csv
import re

class Server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Just Bind the Server
    def Start(address: str, port: int):
        server.bind((address, port))
        server.listen()
    #accept clients
    def Accept():
        global client
        global address
        client, address = server.accept()
        return [client, address]

class Database():
    #delete X line from database
    def Delete(database: str, line: int):
        with open(database) as db:
            lines = db.readlines()
        del lines[line]
    
    def SearchRegex(rule: str, column: int, database: str):
        #compile the rule
        regex = re.compile(rule)
        #r is the list for all the matches
        r = []
        #scan for matches
        with open(database) as db:
            csv_read = csv.reader(db)
            for i in range(len(csv_read)):
                line = csv_read[i]
                search = regex.search(line[column-1])
                if not search is None:
                    r.append(i)
        return r
    
    #Search for a line with little info
    def Search(information: list, columns: list, database: str):
        #init the return list
        ret = []
        #open file
        with open(database) as db:#
            csv_read = csv.reader(db)
            for i in range(len(csv_read)):
                #scan the file
                line = csv_read[i]
                r = True
                for i2 in range(len(columns)):
                    if not line[columns[i2]] == information[i2]:
                        r = False
                #check if all conditions are true
                if r == True:
                    ret.append(i)
        #return
        return ret
    
    def Replace(database: str, line: int, columns: list, updated: list):
        #open
        with open(database) as db:
            #get lines for replacement
            lines = db.readlines()
            #read csv
            csv_read = csv.reader(db)
            replaced = csv_read[line]
            #get X column and X updated in replaced list and replace item
            for i in range(len(columns)):
                replaced[columns[i]] = updated[i]
            #generate csv text
            text = ''
            for i in range(len(replaced)):
                if i == len(replaced)-1:
                    text += str(replaced[i])
                else:
                    text += str(replaced[i])+','
        #replace (Finally)
        lines[line] = text

class Validate():
    def ValidateTextInput(rule: str, string: str):
        pattern = re.compile(rule)
        if pattern.search(string) is None:
            return True
        else:
            return False
    
    def ValidateURL(rules: list, URL: str):
        r = True
        compiled = []
        for rule in rules:
            compiled.append(re.compile(rule))
        for rule in compiled:
            scan = rule.search(URL)
            if not scan is None:
                r = False
        if r == True:
            return False
        else:
            return True