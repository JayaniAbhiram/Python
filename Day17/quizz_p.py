from questionModel import Question
from quizzData import question_data
from quizzBrain import quizz_Brain

questionBank = [ ]

for i in question_data:
    questions = i["text"]
    answers = i["answer"]

    # questionBank.append(questions)
    # questionBank.append(answers)

    newQuestion = Question(questions,answers)
    questionBank.append(newQuestion)


quizz = quizz_Brain(questionBank)
quizz.nextQuestion()

