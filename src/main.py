import sys

try:
    import pygame
except ImportError:
    print("Pygame nicht gefunden. Bitte mit 'pip install pygame-ce' oder 'pacman -S python-pygame' installieren.")
    sys.exit(1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Narayana-Ryoiki: Das Archiv zu Anathot")
    clock = pygame.time.Clock()

    # Pergament-Hintergrundfarbe (#f4e8c1)
    BG_COLOR = (244, 232, 193)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BG_COLOR)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
