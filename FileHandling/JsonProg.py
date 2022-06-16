import json

myJfile=open(r'D:\Devops\CFP\PythonProg\FileHandling\emp.json')
jData=myJfile.read()

object=json.loads(jData)
print(str(object['firstName']))
print(str(object['lastName']))
