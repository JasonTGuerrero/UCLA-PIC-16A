# Name: Jason Guerrero
# UID: 305118489

import re
import urllib.request

#Problem 1:
def mytype(v):
     s1 = re.search(r"^-?\d+$", str(v))                     # int
     s2 = re.search(r"^-?\d+\.\d+$", str(v))                # float
     s3 = re.search(r"\[[\d\,\s]*\]", str(v))               # list
     s4 = re.search(r"(\{[\d\,\s]*\})|(\w*\s*)", str(v))    # string
     if s1 != None and s1.group() == str(v):
          return "int"                            # return int if v is an integer
     elif s2 != None and s2.group() == str(v):
          return "float"                          # return float if v is a float
     elif s3 != None and s3.group() == str(v):
          return "list"                           # return list if v is a list
     elif s4 != None and s4.group() == str(v):
          return "string"                         # return string if v is a string

     pass


# print(mytype(10))
# print(mytype(-10))
# print(mytype(-1.25))
# print(mytype(10.0))
# print(mytype([1, 2, 3]))
# print(mytype([]))
# print(mytype("abc"))
# print(mytype({1,2}))

#Problem 2:
def findpdfs(L):
     pdfFiles = []       # list of pdf files
     for pdf in L:                                # for each possible pdf file in L
          x = re.search(r"\w+\d+.pdf", pdf)
          if x != None and pdf == x.group():      # if it is a pdf
               y = pdf.replace(".pdf", "")
               pdfFiles.append(y)                 # get rid of the .pdf extension and at it to the list of pdf files
          else:
               continue
     
     return pdfFiles

# L = ["IMG2309.jpg", "lecture1.pdf", "homework.py", "homework2.pdf"]
# print(findpdfs(L))


#Problem 3:
def findemail(url):
     emailList = []
     page=urllib.request.urlopen(url).read().decode()
     
     emailList = re.findall(r"\w+@[\w+\.dotDOT\[dot\]\[DOT\]]+", str(page))     # find any emails with @ and .
     x = re.findall(r"\w+\s\w{2}\s\w+\s\w{3}\s\w+\s\w+\s\w{3}", str(page))      # find any emails with tricks
     y = re.findall(r"\w+\[\w+\]\w+\[\w+\]\w+", str(page))                      # find any emails with tricks

     # revert the tricks back to original . and @
     for i in range(len(x)):
          x[i] = x[i].replace(" at ", "@")
          x[i] = x[i].replace(" AT ", "@")
          x[i] = x[i].replace(" dot ", ".")
          x[i] = x[i].replace(" DOT ", ".")


     for i in range(len(y)):
          y[i] = y[i].replace("[at]", "@")
          y[i] = y[i].replace("[AT]", "@")
          y[i] = y[i].replace("[dot]", ".")
          y[i] = y[i].replace("[DOT]", ".")

     
     emailList += x                     #  append the reverted email lists to the list we are returning
     emailList += y
     return list(set(emailList))      # return unique list of emails
     

# url1 = "https://www.math.ucla.edu/~hangjie/contact/"
# url2 = "https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest"
# print(findemail(url1))
# print(findemail(url2))



#Problem 4:
def happiness(text):
     words = text.lower().replace(".","")
     words = words.replace("!","").split()   # get the words as they appear in the file nothing else
     hd = open('/Users/jasonguerrero/Desktop/PIC 16A/happiness_dictionary.py', 'r').read()
     hdRows = re.split(r'\n',hd)   #read file into string
     hdRows[0] = "'laughter':8.5,"
     hdRows.pop()                       #clean up string

     HDROWS = [ch.strip(',') for ch in hdRows]    # get rid of the comments next to the scores 

     L=[re.split(r'(\:\b)(?!.*\1)',i) for i in HDROWS]      # split and the last :

     for i, value in enumerate(L):      # make all the scores floats
          L[i][2] = float(L[i][2])      

     newDict = {}
     for i, j, k in L:        # transfer 2D list into newDict
          newDict[i] = k      

     total_score = 0          # score counter
     n=0                 #word counter
     for word in words:
          word = "'"+word+"'"
          if word in newDict.keys():       # if the word is in the happiness dictionary
               total_score += newDict[word]
               n+=1                          #calculate score and count the word
          else:
               pass
               

     final_score = total_score/n        # compute the average

     return(final_score)


     



# s1 = "Mary had a little lamb."
# s2 = "Mary had a little lamb. Mary had a little lamb!"
# s3 = "A quick brown fox jumps over a lazy dog."

# print(happiness(s1))
# print(happiness(s2))
# print(happiness(s3))
     

