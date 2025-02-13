import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Game")


# Player Properties
player_pos = [400, 300]


# Main game loop
def main():


    # Game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Handle player input
        player_input = pygame.key.get_pressed()

        if player_input[pygame.K_UP]:
            player_pos[1] -= 5
            print("Up key pressed", player_pos)
        if player_input[pygame.K_DOWN]:
            player_pos[1] += 5
            print("Down key pressed", player_pos)
        if player_input[pygame.K_LEFT]:
            player_pos[0] -= 5  
            print("Left key pressed", player_pos)
        if player_input[pygame.K_RIGHT]:
            player_pos[0] += 5
            print("Right key pressed", player_pos)

        

        # Update game state here
        pygame.display.flip()


if __name__ == "__main__":
    main()