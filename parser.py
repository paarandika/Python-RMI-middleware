import sys
try:
    filePath=sys.argv[1]
except:
    print "Argument error"
    exit()

file = open(filePath,"r")
localRef = open("localref.xrnd","r")
remoteRef = open("remoteref.xrnd","r")
outLocal=open("local1.py","w")
outRemote=open("remote1.py","w")

for line in localRef:
    if line=="##1":
        break
    outLocal.write(line)


lineNumber=0
while True:
    temp=file.readline()
    lineNumber+=1
    if temp!="":
        tokens=temp.strip().split("=")
        if len(tokens)<2 or tokens[0]!="base_url":
            print "Error at line ",lineNumber,". base_url not found."
            exit()
        else:
            outLocal.write("base_url=\""+tokens[1]+"\"")
            break
url=""
for line in file:
    lineNumber+=1
    if line!="":
        tokens=line.strip().split("(")
        token1=tokens[0].split()

        if token1[0]=="def":
            args=tokens[1].replace("):","").split(",")
            funcName=token1[1]
            url="/"+funcName
            #outLocal.write("\n\ndef "+funcName+" ( obj ) :")
            outLocal.write("\n\n"+line)
            outLocal.write("\tobj=ObjSkeleton()")
            for arg in args:
                arg=arg.strip()
                outLocal.write("\n\t"+"obj."+arg+"="+arg)
                #outLocal.write("\n\t"+arg+"=obj."+arg)
            print funcName
            print args

        elif token1[0]=="return":
            print url
            outLocal.write("\n\treturn parseJSONtoObj(callMethod(base_url+\""+url+"\",parseObjtoJSON(obj)))")
        else:
            pass
            #outLocal.write("\n\t"+line.strip())




print filePath