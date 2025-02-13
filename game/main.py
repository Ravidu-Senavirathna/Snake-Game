import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Game")


# Main game loop
def main():


    # Game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Update game state here
        pygame.display.flip()


if __name__ == "__main__":
    main()