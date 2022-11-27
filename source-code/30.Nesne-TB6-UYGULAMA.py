
# Question class
class question:
    def __init__(self,text,choices,answer) -> None:
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self,answer):
        return self.answer == answer


# print(q1.checkanswer('Python')) - True
# print(q2.checkanswer('C#')) - False


# Quiz  class
class quiz:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.score = 0
        self.questionindex = 0
        
    def getquestion(self):
        return quiz.questions[self.questionindex]

    def displayquestion(self):
        question = self.getquestion()
        print(f'Soru {self.questionindex + 1}: {question.text}')

        for q in question.choices:
            print('-> ' + q)

        answer = input('Cavap: ')
        self.guess(answer)
        self.loadquestion()

    def guess(self, answer):
        question = self.getquestion()

        if question.checkanswer(answer):
            self.score += 1
        
        self.questionindex += 1

    
    def loadquestion(self):
        if len(self.questions) == self.questionindex:
            self.showscore()
                    
        else:
            self.displayquestion()


    def showscore(self):
        print('Score: ',self.score)


# Soru - seçenekler - cevap
q1 = question('En iyi programlama dili hangisidir ?',['C#','javascript','java','Python'],'Python')
q2 = question('En iyi popüler dili hangisidir ?',['C#','Python','javascript','java'],'Python')
q3 = question('En çok kazandıran programlama dili hangisidir ?',['Python','javascript','C#','java'],'Python')
questions = [q1, q2, q3]

quiz = quiz(questions)

quiz.displayquestion()














