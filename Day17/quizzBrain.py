
from quizz_p import questionBank

class quizz_Brain:
    def __init__(self,qList):
        self.questionNumber = 0
        self.questionList = qList
    
    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber] 
        input(self.questionNumber + " . " + {currentQuestion.text} + "(True or faslse) : ")