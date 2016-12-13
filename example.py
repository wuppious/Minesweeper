import mine
import pygame


def main():  
    # Initialize pygame stuff
    pygame.init()
    screen = pygame.display.set_mode((300,300))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 52)

    # Create our minefield
    minefield = mine.Minefield(10,10,20)

    # Our minefield is 10 x 10 and our screen is 300 x 300
    # so 30px x 30px per slot on the field
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0] // 30 
                y = pos[1] // 30
                print()
                if event.button == 1:
                    if minefield.open(x,y):
                        if minefield.winCondition():
                            running = False
                    else:
                        running = False
                        print(minefield.showMines())
                else:
                    minefield.flag(x,y)
                print(minefield)

            screen.fill((0,0,0))
            for x in range(10):
                for y in range(10):
                    screen.blit(font.render(minefield.board[y][x], True, (255,255,255)), (x*30, y*30))

        pygame.display.flip()
        clock.tick(15)

if __name__ == '__main__':
    main()

