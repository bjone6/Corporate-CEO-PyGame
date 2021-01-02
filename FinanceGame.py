import sys
import pygame
from datetime import date

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
white = (255, 255, 255)
black = (0, 0, 0)

# Load images
boardRoom = pygame.image.load("Board Room.jpg")


# Function to create a button
def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))


# Start menu returns true until we click the Start button
def start_menu():
    startText = font.render("The Corporate CEO", True, slategrey)
    today = date.today()
    todayText = "Today is " + today.strftime("%A") + ", " + today.strftime("%B") + " " + today.strftime("%d") + \
                ", " + today.strftime("%Y")
    todayText = smallfont.render(todayText, True, slategrey)

    while True:
        screen.fill((0, 0, 0))
        # (image variable, (left, top))
        screen.blit(todayText, (5, 10))
        # The Corporate CEO centered Text
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        # start button (left, top, width, height)
        start_button = create_button(screen_width - 130, 7, 125, 26, lightgrey, slategrey)

        if start_button:
            game_menu()

        # Start button text
        startbuttontext = smallfont.render("Start the Game!", True, blackish)
        screen.blit(startbuttontext, (screen_width - 125, 9))

        # Displays the board room picture
        screen.blit(boardRoom, (1, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
        return True


def game_menu():
    startText = font.render("The Corporate CEO", True, slategrey)
    newCEOText = font.render("NEW CEO", True, blackish)
    loadCEOText = font.render("LOAD CEO", True, blackish)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        # button (left, top, width, height)
        newCEOButtton = create_button((screen_width / 2) - 100, int(screen_height * .33), 200, 50, lightgrey, slategrey)

        if newCEOButtton:
            new_game()

        # New CEO button text
        screen.blit(newCEOText, ((screen_width / 2) - (newCEOText.get_width() / 2), int(screen_height * .33)))

        loadCEOButtton = create_button((screen_width / 2) - 100, screen_height / 2, 200, 50, lightgrey, slategrey)

        if loadCEOButtton:
            print("Load CEO button clicked.")

        # Load CEO button text
        screen.blit(loadCEOText, ((screen_width / 2) - (newCEOText.get_width() / 2), screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


def new_game():
    startText = font.render("The Corporate CEO", True, slategrey)
    newUserName = ""

    # Used to make the text grey and white when active
    nameActive = False
    regionsActive = False
    petroActive = False
    beairdActive = False

    # Declare Variables
    careerChoicePrompt = font.render("Choose Your Career", True, slategrey)
    regionsTower = pygame.image.load("Regions Tower.jpg")
    petroTower = pygame.image.load("Petro Tower.jpg")
    beairdTower = pygame.image.load("Beaird Tower.jpg")

    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        # Create the text box
        userNameSurface = font.render(newUserName, True, white)

        # Create the border around the text box with .Rect
        # left, top, width, height
        userNameBorder = pygame.Rect(((screen_width - userNameSurface.get_width()) / 2) - 10, screen_height * .20,
                                     userNameSurface.get_width() + 10, 50)

        # This is the text surface when the user types in their name
        screen.blit(userNameSurface, ((screen_width - userNameSurface.get_width()) / 2, screen_height * .20))

        # Create the borders around the career pictures
        regionsBorder = pygame.Rect((screen_width * .075) - 4, (screen_height * .45) - 4, regionsTower.get_width() + 8,
                                    regionsTower.get_height() + 8)

        petroBorder = pygame.Rect((screen_width - petroTower.get_width())/ 2 - 4, (screen_height * .45) - 4,
                                  petroTower.get_width() + 8, petroTower.get_height() + 8)

        beairdBorder = pygame.Rect(((screen_width - beairdTower.get_width()) * .9) - 4, (screen_height * .45) - 4,
                                   beairdTower.get_width() + 8, beairdTower.get_height() + 8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse and Keyboard events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if userNameBorder.collidepoint(event.pos):
                    nameActive = True
                elif regionsBorder.collidepoint(event.pos):
                    regionsActive = True
                elif petroBorder.collidepoint(event.pos):
                    petroActive = True
                elif beairdBorder.collidepoint(event.pos):
                    beairdActive = True
                else:
                    nameActive = False
                    regionsActive = False
                    petroActive = False
                    beairdActive = False

            if event.type == pygame.KEYDOWN:
                if nameActive:
                    if event.key == pygame.K_BACKSPACE:
                        newUserName = newUserName[:-1]
                    else:
                        newUserName += event.unicode

        # Handles the click events by swtiching from white, slategrey, and black
        if nameActive:
            pygame.draw.rect(screen, white, userNameBorder, 2)
            userNamePrompt = font.render("Enter your first and last name here", True, white)
        else:
            pygame.draw.rect(screen, slategrey, userNameBorder, 2)
            userNamePrompt = font.render("Enter your first and last name here", True, slategrey)

        if regionsActive:
            investment = font.render("Investment Co.", True, white)
            pygame.draw.rect(screen, white, regionsBorder, 2)
            petroActive = False
            beairdActive = False
        else:
            investment = font.render("Investment Co.", True, slategrey)
            pygame.draw.rect(screen, black, regionsBorder, 2)

        if petroActive:
            gasAndOil = font.render("Gas & Oil", True, white)
            pygame.draw.rect(screen, white, petroBorder, 2)
            regionsActive = False
            beairdActive = False
        else:
            gasAndOil = font.render("Gas & Oil", True, slategrey)
            pygame.draw.rect(screen, black, petroBorder, 2)

        if beairdActive:
            realEstate = font.render("Real Estate", True, white)
            pygame.draw.rect(screen, white, beairdBorder, 2)
            regionsActive = False
            petroActive = False
        else:
            realEstate = font.render("Real Estate", True, slategrey)
            pygame.draw.rect(screen, black, beairdBorder, 2)

        screen.blit(userNamePrompt, ((screen_width - userNamePrompt.get_width()) / 2,
                                     (screen_height * .20) + userNameSurface.get_height()))

        screen.blit(careerChoicePrompt, ((screen_width - careerChoicePrompt.get_width()) / 2, screen_height * .35))

        # Choose your Career Pictures
        screen.blit(regionsTower, (screen_width * .075, screen_height * .45))
        screen.blit(investment, ((screen_width + investment.get_width()) * .075, screen_height * .80))

        screen.blit(petroTower, ((screen_width - petroTower.get_width()) / 2, screen_height * .45))
        screen.blit(gasAndOil, ((screen_width - gasAndOil.get_width()) / 2, screen_height * .80))

        screen.blit(beairdTower, ((screen_width - beairdTower.get_width()) * .9, screen_height * .45))
        screen.blit(realEstate, ((screen_width - realEstate.get_width()) * .875, screen_height * .80))

        pygame.display.update()
        clock.tick(15)


# Game loop
while True:
    start_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(15)

