import smtplib
import json
#To mail, be sure that less-secure apps is allowed on your Gmail.
questions = True

quizBank ={

}

#Get answer to a question function
#Takes in an input and searches the quizBank keys
#If question is in quizBank.keys() output answer to that question
#If not, list the questions in the quizBank for the user

def getAnswer():
    getAnswer = input("What question would you like the answer to?: ")
    if getAnswer in quizBank.keys():
        print(quizBank[getAnswer])

    else:
        print('That question does not exist, here are the list of questions: ')
        for questions in quizBank.keys():
            print(questions)
    getQuestion()


#Define a getQuestion function that allows the user to input a question they want to put in the question bank
#Give the user options to either quit, get an answer to a question, or mail themselves the question bank
#Print out the question bank using variable quizBank
def getQuestion():
    global questions
    while questions:
        print("If you want to mail your question bank, type 'mail'")
        print("If you want to quit, enter 'quit'")
        print("If you want an answer to a question, enter 'answer'")
        userInputQuestions = input( "Enter a question to be quizzed on: ")
        if userInputQuestions.lower() == 'quit':
            questions = False
            break
        elif userInputQuestions.lower() == 'answer':
            getAnswer()
            break
        elif userInputQuestions.lower() == 'mail':

            sender_email = input(str("Enter an email to send the mail: "))
            rec_email = input(str("Enter an email to receive the mail: "))
            password = input(str("Enter your password for the email that is sending the questions: "))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print("LOGIN SUCCESS")
            server.sendmail(sender_email, rec_email, json.dumps(quizBank,indent=4))
            print("EMAIL HAS BEEN SENT!!")
            getQuestion()
            break
        userInputAnswer = input("What is the answer to the question you entered?: ")
        quizBank[userInputQuestions] = userInputAnswer
        print(quizBank)


print(getQuestion())

