import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

def playsound(soundname):
    sounds = pygame.mixer
    sounds.init()
    
    s = sounds.Sound(soundname)
    wait_finish(s.play())
    
hostchoice = 0
questionsasked = 0
answersright = 0
answerswrong = 0

while hostchoice != 3:

    hostchoice = int(input("Was the answer (1) right, (2) wrong or (3) is the game over? (1/2/3)"))
                         
    if hostchoice == 1:
        playsound("heartbeat.wav")
        playsound("correct.wav")
        questionsasked = questionsasked + 1
        answersright = answersright + 1

    if hostchoice == 2:
        playsound("heartbeat.wav")
        playsound("wrong.wav")
        questionsasked = questionsasked + 1
        answerswrong = answerswrong + 1

print("Total questions asked:   " + str(questionsasked))
print("Total right answers:     " + str(answersright))
print("Total wrong answers:     " + str(answerswrong))
playsound("applause.wav")
