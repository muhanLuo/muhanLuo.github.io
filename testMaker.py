import json

def createMC(optionArray):
    finalHTML = ""
    
    for option in optionArray:
        finalHTML+="<li>{}</li>".format(option)
        
    return ("<ol type=A>" + finalHTML + "</ol>")



f = open("quiz.json","r")
o = open("output.html","w")

quizDict = json.loads(f.read())
questions = quizDict["content"]

# Formatting
o.writelines("<html>")
o.writelines("<title>{0}</title><h1>{0}</h1>".format(quizDict["title"]))
o.writelines("<h2>Name: " + "_"*20 + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date:" + "_"*10 + "</h2>")


questionCounter = 1
for questNumber in questions:
    
    o.write("<h3>{0}. {1}</h3>".format(str(questionCounter),questions[questNumber]["content"]))
    
    # Creates Multiple Choice Questions
    if questions[questNumber]["type"] == "MC":
        o.write(createMC(questions[questNumber]["options"]))
    
    elif questions[questNumber]["type"] == "Short":
        pass
    questionCounter+=1


# End Formatting
o.writelines("</html>")