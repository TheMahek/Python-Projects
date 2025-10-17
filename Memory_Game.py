import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle 🃏")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 150, 255)
GREEN = (0, 200, 100)

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Card settings
CARD_SIZE = 80
PADDING = 10
ROWS, COLS = 4, 4  # 4x4 grid

# Create pairs of numbers (8 pairs)
cards = list(range(1, 9)) * 2
random.shuffle(cards)

# Grid with positions
grid = []
for row in range(ROWS):
    for col in range(COLS):
        grid.append({
            "value": cards[row * COLS + col],
            "rect": pygame.Rect(col * (CARD_SIZE + PADDING) + PADDING,
                                row * (CARD_SIZE + PADDING) + PADDING,
                                CARD_SIZE, CARD_SIZE),
            "flipped": False,
            "matched": False
        })

def draw_cards():
    for card in grid:
        if card["flipped"] or card["matched"]:
            pygame.draw.rect(screen, GREEN, card["rect"])
            text = font.render(str(card["value"]), True, BLACK)
            text_rect = text.get_rect(center=card["rect"].center)
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, BLUE, card["rect"])

def main():
    running = True
    first_card = None
    second_card = None
    matches_found = 0

    while running:
        screen.fill(WHITE)
        draw_cards()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                for card in grid:
                    if card["rect"].collidepoint(pos) and not card["flipped"] and not card["matched"]:
                        if first_card is None:
                            card["flipped"] = True
                            first_card = card
                        elif second_card is None:
                            card["flipped"] = True
                            second_card = card

        if first_card and second_card:
            pygame.display.flip()
            pygame.time.delay(800)  # pause to show second card

            if first_card["value"] == second_card["value"]:
                first_card["matched"] = True
                second_card["matched"] = True
                matches_found += 1
            else:
                first_card["flipped"] = False
                second_card["flipped"] = False

            first_card = None
            second_card = None

        if matches_found == 8:  # all pairs matched
            screen.fill(WHITE)
            win_text = font.render("🎉 You Win!", True, BLACK)
            screen.blit(win_text, (WIDTH // 3, HEIGHT // 2))
            pygame.display.flip()
            time.sleep(2)
            running = False

    pygame.quit()

# Run game
main()
