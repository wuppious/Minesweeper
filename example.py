import mine
import pygame


def main():  
    pygame.init()
    screen = pygame.display.set_mode((300,300))
    clock = pygame.time.Clock()
    running = True
    
    minefield = mine.Minefield(10,10,20)
    font = pygame.font.Font(None, 52)

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

