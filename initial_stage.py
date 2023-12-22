import speech_recognition as sr
import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Voice-controlled Snake Game")

# Set up snake properties
snake_size = 20
snake_speed = 15
x, y = width // 2, height // 2
x_change, y_change = 0, 0

# Initialize SpeechRecognition
recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Say a command:")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Google Speech Recognition request failed: {e}")
        return None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    command = listen_for_command()

    if command:
        if "left" in command:
            x_change = -snake_size
            y_change = 0
        elif "right" in command:
            x_change = snake_size
            y_change = 0
        elif "up" in command:
            x_change = 0
            y_change = -snake_size
        elif "down" in command:
            x_change = 0
            y_change = snake_size

    # Update snake position
    x += x_change
    y += y_change

    # Draw the snake on the screen
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, snake_size, snake_size))
    pygame.display.update()

    # Adjust the snake speed
    time.sleep(1/snake_speed)

pygame.quit()

    
