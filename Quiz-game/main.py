from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank=[]
for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = Question(question_text,question_answer)
    Question_bank.append(new_question)

quiz=QuizBrain(Question_bank)

while quiz.stil_has_question():
      quiz.next_question()
