import json

def txtdata():
    try:
        """
        filename=path/filename.extension
        example: /home/data/testdata.txt
        """
        with open("testdata.txt", 'r') as filedata:
            """
            Intertively accessing data instead of loading all data in RAM.
            It help you to load 100GB of file with 8GB of RAM.
            """
            for line in filedata:
                """
                Here you get each lien from text and you can process it.
                Variable name is "line"
                """
                print(line)
    except Exception as e:
        print("Error: "+e)
    filedata.close()

def jsondata():
    try:
        """
        filename=path/filename.extension
        example: /home/data/testdata.json
        """
        with open(filename, 'r') as filedata:
            """
            Intertively accessing data instead of loading all data in RAM.
            It help you to load 100GB of file with 8GB of RAM.
            """
            for jsonobject in filedata:
                try:
                    """
                    Here you get each object from json and you can process as python dictonary.
                    Variable name is "one_dic"
                    """
                    one_dic = json.loads(jsonobject)
                except Exception as e:
                    print("Error :"+e)
    except Exception as e:
        print("Error :"+e)
    filedata.close()

if __name__=="__main__":
    txtdata()
