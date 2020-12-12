import sys
import pygame
# Used to get stock information
import yfinance as yf

# Initializing
pygame.init()

# Setting Clock
clock = pygame.time.Clock()

# Create the screen
screen_width = 1070
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Financial Game")

# Initialize constants
font = pygame.font.SysFont("comicsansms", 30)
smallfont = pygame.font.SysFont("comicsansms", 14)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)

# Load images
boardRoom = pygame.image.load("Board Room.jpg")

# Getting stock information once
sandp = yf.Ticker("^GSPC")
sandpPrice = str(sandp.info['ask'])
dow = yf.Ticker("^DJI")
dowPrice = str(dow.info['ask'])


# Function to create a button
def create_button(msg, x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            first_level()
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))
    # Start button text
    startbuttontext = smallfont.render(msg, True, blackish)
    screen.blit(startbuttontext, (int(890 + (width / 2)), int(y + (y / 2))))


# Start menu returns true until we click the Start button
def start_menu(sandpPrice, dowPrice):
    startText = font.render("The Corporate CEO", True, slategrey)
    # Get market data
    sandpPrice = smallfont.render("S&P 500: " + sandpPrice, True, slategrey)
    dowPrice = smallfont.render("DOW: " + dowPrice, True, slategrey)

    while True:
        screen.fill((0, 0, 0))
        # (image variable, (left, top))
        screen.blit(sandpPrice, (5, 0))
        screen.blit(dowPrice, (5, sandpPrice.get_height()))
        # The Corporate CEO centered Text
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        # start button (left, top, width, height)
        create_button("Start Your Day!", screen_width - 130, 7, 125, 26, lightgrey, slategrey)

        # Displays the board room picture
        screen.blit(boardRoom, (1, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
        return True


def first_level():
    startText = font.render("The Corporate CEO", True, slategrey)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


# Game loop
while True:
    start_menu(sandpPrice, dowPrice)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(15)

