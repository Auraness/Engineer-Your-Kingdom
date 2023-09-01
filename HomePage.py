import pygame

from pygame.locals import (
    RLEACCEL,
    KEYDOWN,
    QUIT,
    K_ESCAPE,
    K_SPACE,
    K_a,
    K_b,
    K_c,
    K_d
)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    run = True
    while run:
        green = (184, 227, 186)
        black = (0, 0, 0)
        screen.fill(green)

        font = pygame.font.SysFont("Times New Roman", 32, bold=False, italic=False)
        text = font.render("Welcome to Engineer Your Kingdom!", True, black, green)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text, textRect)

        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Please press the space button to continue.", True, black, green)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50)
        screen.blit(text, textRect)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    break
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                break

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\logo.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 32, bold=False, italic=False)
        text = font.render("Here, we will learn what engineering is and", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 32, bold=False, italic=False)
        text = font.render("some basic facts about engineering", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 32, bold=False, italic=False)
        text = font.render("Are you ready?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##1 STAR
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Engineering is essentially using all types of science", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("to solve problems and make things that already exist better.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Q1: What doesn’t count as engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("A. Making a cup holder", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("B. Fixing a chair", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("C. Curling your hair", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("D. Making a robot", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_c:
                    run = False
                if event.key != K_c:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\1 star.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("SURPRISE!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("If you get the questions right,", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("you get to build a kingdom!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##2 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What are the types of engineers?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Engineering is a very broad field. There are biochemical engineers,", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("electrical engineers, agricultural engineers, etc. Anyone can be an engineer!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Q2: What fields don’t need engineers?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("A. Hair stylists", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("B. Astronauts", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("C. Farmers", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("D. None of the above", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_d:
                    run = False
                if event.key != K_d:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\2 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("2 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Now you get towers", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("inside your moat!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##3 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What tools do engineers use?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Since engineering is such a broad field, engineers use all sorts of tools.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("They can use hammers, screwdrivers, and drills.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("They can also use microscopes, hoes, and pipettes!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Q3: Can an engineer use all of these in their job? [3D printer, calculator, comb, paper, ruler]", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Yes", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. No", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_b:
                    run = False
                if event.key != K_b:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\3 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("3 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get accessories", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("like flags and windows!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##4 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is civil engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Civil engineering is a professional discipline that deals with the physical", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("and naturally built environment, including public works such as roads and bridges.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q4: What can civil engineers not work on?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Buildings", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. Boats", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. Dams", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. Sewers", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_b:
                    run = False
                if event.key != K_b:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\4 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("4 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get knights", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("to protect your castle!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##5 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is mechanical engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Mechanical engineering studies physical machines.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("It combines physics and math to work on machines.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Q5: Will the work that mechanical engineers do go to these places?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("[Space, the ocean, the rainforest]", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Yes", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. No", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_b:
                    run = False
                if event.key != K_b:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\5 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("5 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get a lake", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("for your fish!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##6 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is electrical engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Electrical engineering is the discipline that works", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("with electricity, electronics, and electromagnetism.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q6: What is electricity directed through?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Electric board", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. Floppy disk", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. Wire desk", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. Circuit", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_d:
                    run = False
                if event.key != K_d:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\6 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("6 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get farmland", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("for food!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
    
    ##7 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is computer engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Computer engineering is a branch of electrical engineering.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("It connects computer science to electrical engineering.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q7: What do computer engineers not do?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Build phones", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. Build laptops", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. Code apps", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. None of the above", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_d:
                    run = False
                if event.key != K_d:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\7 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("7 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get farmers", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("to make food!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##8 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is chemical engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Chemical engineering is the branch of engineering that", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("builds and designs industrial chemical plants.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q8: What is the chemical formula for water?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. HO2", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. H2O2", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. H2O", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. HO", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_c:
                    run = False
                if event.key != K_c:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\8 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("8 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get crops!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("The farmers did their job well.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
    
    ##9 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is biomedical engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Biomedical engineers focus on building new machines", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("and technology to further advance the medical industry.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 20, bold=False, italic=False)
        text = font.render("Q9: Which place would you see the work of a biomedical engineer?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. School", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. House", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. Park", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. Beach", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_a:
                    run = False
                if event.key != K_a:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\9 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("9 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get small houses", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("in your city!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    ##10 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("What is genetic engineering?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Genetic engineering is related to biomedical engineering.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("These engineers deliberately change the characteristics of an", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("organism by manipulating their genetic material.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q10: What is the genetic material in living organisms?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. NDA", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. DNA", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. AND", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. DAN", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_b:
                    run = False
                if event.key != K_b:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\10 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("10 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get market", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("to buy things!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
    
    ##11 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Mass versus weight!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Mass and weight are commonly confused terms in science.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Mass measures how much matter something contains.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Weight measures the gravitational force on an object.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Q11: What measurement stays the same on Earth and on the moon??", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Weight", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. Mass", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_b:
                    run = False
                if event.key != K_b:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\11 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("11 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get a port", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("for your boats!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
    
    ##12 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Safety", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("Safety is always the main priority in any field. In engineering,", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("it is important to be careful of machines and chemicals", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("as you could get seriously hurt if you don’t.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q12: What can’t you use as a safety measure?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Bracelet", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. Mask", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. Hemlet", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. Apron", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_a:
                    run = False
                if event.key != K_a:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\12 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("12 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get boats", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("to fish!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
    
    ##13 STARS
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("How to become an engineer?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("There are endless ways to become an engineer since", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render(" there are so many branches but the main thing to keep in", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 16, bold=False, italic=False)
        text = font.render("mind is to be passionate and never give up!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()
        
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Q13: In the process of building this game, what did I not do?", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 110)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Please press the correct answer letter on your keyboard.", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 80)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("A. Code", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("B. Create a plan on paper", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("C. Draw pictures", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("D. None of the above", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 100)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_b:
                    run = False
                if event.key != K_b:
                    quit()

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\13 stars.png").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        screen.fill(green)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("13 STARS", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 50)
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("Now you get to go", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        font = pygame.font.SysFont("Times New Roman", 25, bold=False, italic=False)
        text = font.render("venture out and build your kingdom!", True, black, green)
        textRect = text.get_rect()
        textRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 50)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()

    run = True
    while run:
        imp = pygame.image.load("C:\\Users\\aurac\\Downloads\\Game\\end.jpg").convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_SPACE:
                    run = False

            elif event.type == QUIT:
                quit()