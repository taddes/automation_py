#! python3
""" randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.
"""

import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

            
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizdir = os.path.join(os.getcwd(), 'qizzes')
    # os.makedirs(quizdir)
    answerdir = os.path.join(os.getcwd(), 'answers')
    # os.makedirs(answerdir)
    quizFile = open(quizdir + f'/capitalsquiz{quizNum + 1}.txt', 'w')
    answerkey = open(answerdir + f'/capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # TODO: Write out the header for the quiz.
    quizFile.write((' ' * 20) + f'State Capitals Quiz No. {quizNum + 1}')
    quizFile.write('\n\n')
    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correct_answer = capitals[states[questionNum]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}\n')
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quizFile.write('\n')
        answerkey.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answer_options.index(correct_answer)]))
    quizFile.close()
    answerkey.close()
