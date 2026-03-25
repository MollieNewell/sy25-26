import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False




# Trail properties
player_trail = []  # List to store previous positions
trail_length = 20  # Maximum number of trail segments






while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- BUG 1: Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Should move right

    # Update enemy position
    enemy_pos[1] += enemy_speed

     # --- BUG 2: Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        # The enemy should go back to the top with a new X position
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")




                # Increase player size
        player_size += 5
        # Adjust player position to keep it centered
        player_pos[0] = max(0, min(player_pos[0], WIDTH - player_size))
        player_pos[1] = HEIGHT - 50




        # --- BUG 3: Collision Detection ---
    # Corrected logic for rectangular collision detection
    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True







  # Update trail
    player_trail.append((player_pos[0], player_pos[1]))
    if len(player_trail) > trail_length:
        player_trail.pop(0)

    # Drawing
    screen.fill((0, 0, 0))

    # Draw the trail with decreasing transparency
    for i, trail_pos in enumerate(player_trail):
        alpha = int(255 * (i / trail_length))  # Calculate transparency
        trail_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
        trail_surface.fill((*BLUE, alpha))  # Add alpha to the color
        screen.blit(trail_surface, trail_pos)






    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
