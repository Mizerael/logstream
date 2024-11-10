import pygame
import sys


def win(mas, sign, text="Победа"):
    zeroes = 0
    resp_str = f"{text}:{sign}"
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return resp_str
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return resp_str
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return resp_str
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return resp_str
    if zeroes == 0:
        return "Ничья"
    return False


pygame.init()

size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height)
path_to_background_image = "source/backgorund.png"

screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tak-Toe")

background_image = pygame.image.load(path_to_background_image)
background_image = pygame.transform.scale(background_image, size_window)

cell_color = (204, 204, 106)
cross_color = (66, 47, 39)
circle_color = (76, 173, 24)
winner_color = (0, 0, 0, 0)

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                game_over = False
                mas = [[0] * 3 for i in range(3)]
                query = 0
            else:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse // (margin + size_block)
                row = y_mouse // (margin + size_block)
                if mas[row][col] == 0:
                    if query % 2 == 0:
                        mas[row][col] = "x"
                    else:
                        mas[row][col] = "o"
                    query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0

    screen.blit(background_image, (0, 0))
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == "x":
                    color = cross_color
                elif mas[row][col] == "o":
                    color = circle_color
                else:
                    color = cell_color
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == cross_color:
                    pygame.draw.line(
                        screen,
                        cell_color,
                        (x + 5, y + 5),
                        (size_block + x - 5, size_block + y - 5),
                        5,
                    )
                    pygame.draw.line(
                        screen,
                        cell_color,
                        (x + size_block - 5, y + 5),
                        (x + 5, size_block + y - 5),
                        5,
                    )
                elif color == circle_color:
                    pygame.draw.circle(
                        screen,
                        cell_color,
                        (x + size_block // 2, y + size_block // 2),
                        size_block // 2 - 3,
                        3,
                    )
    if (query - 1) % 2 == 0:
        game_over = win(mas, "x")
        winner_color = cross_color
    else:
        game_over = win(mas, "o")
        winner_color = circle_color

    if game_over:
        screen.fill(winner_color)
        font = pygame.font.SysFont("stxingkai", 80)
        text = font.render(game_over, True, cell_color)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    pygame.display.update()
