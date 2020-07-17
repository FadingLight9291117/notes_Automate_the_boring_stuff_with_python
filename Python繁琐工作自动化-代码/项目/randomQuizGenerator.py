#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

'''
    项目8.5 生成随机的测试文件
'''

import random, os

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

if not os.path.exists('./files'):
    os.makedirs('./files')

# Generator 35 quiz files.
for quizNum in range(35):
    # create the quiz and answer key files.
    quizFile = open('./files/captialsquiz%s.txt' % (quizNum + 1), 'w') # open不能创建目录
    answerKeyFile = open('./files/captialsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Captial Quiz (From %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)  # 重新排列list顺序

    # Loop through all 50 states, making a question for each.
    for questionNum in range(len(states)):

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())  # 获取错误答案列表
        wrongAnswers.remove(correctAnswer)  # 去除正确答案
        wrongAnswers = random.sample(wrongAnswers, 3)   # 选择3个元素即错误答案

        asnwerOptions = wrongAnswers + [correctAnswer]  # 错误答案列表加上正确答案共4个选项
        random.shuffle(asnwerOptions)   # 重新排序

        # write the question and options to the quiz file.
        quizFile.write('%s. What is the captial of %s?\n' % ((questionNum + 1), states[questionNum]))
        for i in range(4):
            quizFile.write((' ') * 4 + '%s. %s\n' % ('ABCD'[i], asnwerOptions[i]))
        quizFile.write('\n')

        # write the answer key to a  file.
        answerKeyFile.write('%s. %s\n' % ((questionNum + 1), 'ABCD'[asnwerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
