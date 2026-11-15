import pygame
from random import choice
pygame.init()
window_w = 500
window_h = 500
window = pygame.display.set_mode((window_w, window_h))
background = (255,255,255)
window.fill(background)
clock = pygame.time.Clock()
LIGHT_YELLOW = (253, 255, 133)
BLACK = (0, 0, 0)

class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

#установить текст на карточке

    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)

#отобразить карточку

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

quest_card = TextArea(120, 100, 290, 70, LIGHT_YELLOW)
quest_card.set_text('Вопрос',65)

answer_card = TextArea(120, 240, 290, 70, LIGHT_YELLOW)
answer_card.set_text('Ответ',65)

quests = ['Что изучаешь в алгоритмике?', 'Чем занимаешься в свободное время?', 'Какое время года любишь?']
answers = ['Python', 'Отдыхаю', 'Лето']

quest_card.draw(10,10)
answer_card.draw(10,10)

#глав игровой цикл
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                question = choice(quests)
                quest_card.set_text(question, 25)
                quest_card.draw(10,10)
            if event.key == pygame.K_a:
                answer = choice(answers)
                answer_card.set_text(answer, 25)
                answer_card.draw(10,10)

    clock.tick(40)
    pygame.display.update()
