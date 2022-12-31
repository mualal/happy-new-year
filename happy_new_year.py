import turtle


def to_given_position(canv, x, y):
    """
    переставляет перо в точку с заданными координатами
    :param canv: объект Turtle, с помощью которого рисуем
    :param x: координата x
    :param y: координата y
    :return: None
    """
    canv.penup()
    canv.goto(x, y)
    canv.pendown()

    return None


def christmas_tree(canv):
    """
    рисует новогоднюю ёлку
    :param canv: объект (грифель) Turtle, с помощью которого рисуем
    :return: None
    """
    to_given_position(canv, 0, 0)
    canv.pensize(1.4)
    n = 100  # масштаб
    canv.speed('fastest')
    canv.left(90)
    canv.forward(3 * n)
    canv.color('dark green')
    canv.backward(n * 4.8)

    def tree(d, s):
        if d <= 0:
            return
        canv.forward(s)
        tree(d - 1, s * .8)
        canv.right(120)
        tree(d - 3, s * .5)
        canv.right(120)
        tree(d - 3, s * .5)
        canv.right(120)
        canv.backward(s)

    tree(15, n)
    canv.backward(n / 5)

    return None


def snowflake(canv, length, depth, snowflake_color, segment_width):
    """
    рисует снежинку
    :param canv: объект Turtle, с помощью которого рисуем
    :param length: длина элемента снежинки
    :param depth: глубина дерева снежинки
    :param snowflake_color: цвет снежинки
    :param segment_width: толщина линий
    :return:
    """
    canv.color(snowflake_color)
    canv.pensize(segment_width)
    if depth > 0:
        for _ in range(6):
            canv.forward(length)
            snowflake(draw_snowflake, length // 3, depth - 1, snowflake_color, segment_width)
            canv.backward(length)
            canv.left(60)
    return None


def stars(canv, scale):
    canv.setheading(0)
    for _ in range(3):
        canv.begin_fill()
        for _ in range(5):
            canv.forward(30 / scale)
            canv.right(144)
        canv.end_fill()
        canv.penup()
        canv.forward(90 / scale)
        canv.pendown()
    return None


def sphere(canv, x, y, scale, sphere_color, zigzag_color, circles_color, stars_color):
    """
    рисует ёлочные сферы
    :param canv: объект Turtle, с помощью которого рисуем
    :param x: координата x сферы
    :param y: координата y сферы
    :param scale: пропорциональное увеличение расмера сферы и всех объектов на ней
    :param sphere_color: цвет сферы
    :param zigzag_color: цвет зигзагов
    :param circles_color: цвет шариков
    :param stars_color: цвет звёздочек
    :return: None
    """
    scale **= -1

    to_given_position(canv, 0/scale + x, 250/scale + y)
    canv.color("darkkhaki")
    canv.pensize(10 / scale)
    canv.right(90)
    canv.forward(100 / scale)

    # крепление сферы к ёлке
    canv.pensize(1 / scale)
    canv.right(90)
    canv.back(20 / scale)
    canv.begin_fill()
    for _ in range(2):
        canv.forward(40 / scale)
        canv.left(90)
        canv.forward(10 / scale)
        canv.left(90)
    canv.end_fill()

    # круг
    to_given_position(canv, 0/scale + x, 140/scale + y)
    canv.color(sphere_color)
    canv.begin_fill()
    canv.circle(200 / scale)
    canv.end_fill()

    # зигзаг 1 на сфере
    to_given_position(canv, 176/scale + x, 30/scale + y)
    canv.color(zigzag_color)
    canv.pensize(3 / scale)
    canv.left(45)
    for _ in range(5):
        canv.forward(50 / scale)
        canv.right(90)
        canv.forward(50 / scale)
        canv.left(90)

    # круги на сфере
    to_given_position(canv, -160/scale + x, -65/scale + y)
    canv.color(circles_color)
    canv.left(135)
    canv.begin_fill()
    for _ in range(5):
        canv.circle(10 / scale)
        canv.penup()
        canv.forward(80 / scale)
        canv.pendown()
    canv.end_fill()

    # зигзаг 2 на сфере
    to_given_position(canv, -185/scale + x, -135/scale + y)
    canv.color(zigzag_color)
    canv.left(45)
    for _ in range(5):
        canv.forward(50 / scale)
        canv.right(90)
        canv.forward(50 / scale)
        canv.left(90)
    canv.forward(35 / scale)

    # звёздочки 1 на сфере
    to_given_position(canv, -105/scale + x, 80/scale + y)
    canv.pensize(1)
    canv.color(stars_color)
    stars(canv, scale)

    # звёздочки 2 на сфере
    to_given_position(canv, -105/scale + x, -180/scale + y)
    stars(canv, scale)

    return None


def box(canv, x, y, scale, box_color, band_color):
    """
    рисует упаковку для подарков
    :param canv: объект Turtle, с помощью которого рисуем
    :param x: координата x упаковки
    :param y: координата y упаковки
    :param scale: пропорциональное увеличение расмера упаковки и всех объектов на ней
    :param box_color: цвет упаковки
    :param band_color: цвет лент на упаковке
    :return:
    """
    scale **= -1

    canv.setheading(0)
    # крышка подарка
    to_given_position(canv, -180 / scale + x, 20 / scale + y)
    canv.color(box_color)
    canv.begin_fill()
    for _ in range(2):
        canv.forward(360 / scale)
        canv.left(90)
        canv.forward(60 / scale)
        canv.left(90)
    canv.end_fill()

    # коробка
    to_given_position(canv, -160 / scale + x, 0 / scale + y)
    canv.begin_fill()
    for _ in range(2):
        canv.forward(320 / scale)
        canv.right(90)
        canv.forward(210 / scale)
        canv.right(90)
    canv.end_fill()

    # лента 1 подарка
    to_given_position(canv, -10 / scale + x, 80 / scale + y)
    canv.color(band_color)
    canv.begin_fill()
    for _ in range(2):
        canv.forward(15 / scale)
        canv.right(90)
        canv.forward(290 / scale)
        canv.right(90)
    canv.end_fill()

    # лента 2 подарка
    to_given_position(canv, -160 / scale + x, 0 / scale + y)
    canv.color(band_color)
    canv.begin_fill()
    canv.left(90)
    for _ in range(2):
        canv.forward(15 / scale)
        canv.right(90)
        canv.forward(320 / scale)
        canv.right(90)
    canv.end_fill()

    # узел 1 ленты
    to_given_position(canv, 10 / scale + x, 100 / scale + y)
    canv.right(90)
    canv.pensize(10 / scale)
    canv.color(box_color)
    for _ in range(90):
        canv.forward(1 / scale)
        canv.left(0.4)
    for _ in range(90):
        canv.forward(1 / scale)
        canv.left(2)
    for _ in range(90):
        canv.forward(1 / scale)
        canv.left(0.4)

    # узел 2 ленты
    to_given_position(canv, -10 / scale + x, 100 / scale + y)
    canv.right(70)
    for _ in range(90):
        canv.forward(1 / scale)
        canv.right(0.4)
    for _ in range(90):
        canv.forward(1 / scale)
        canv.right(2)
    for _ in range(90):
        canv.forward(1 / scale)
        canv.right(0.4)

    return None


if __name__ == '__main__':

    screen = turtle.Screen()
    screen.bgcolor('light blue')  # настройка фонового цвета

    # задаём 5 грифелей для рисования разных объектов
    draw_tree = turtle.Turtle()
    draw_snowflake = turtle.Turtle()
    draw_text = turtle.Turtle()
    draw_balls = turtle.Turtle()
    draw_gift = turtle.Turtle()

    # рисуем 2 подарка
    box(draw_gift, 100, -200, 1/7, 'blue', 'yellow')
    box(draw_gift, -40, -177, 1/7, 'orange', 'blue')

    # рисуем украшение для новогодней ёлки
    to_given_position(draw_snowflake, 0, 305)
    snowflake(draw_snowflake, 20, 2, 'yellow', 2)

    # рисуем ёлочные сферы, которые будут скрываться за ветками ёлки
    sphere(draw_balls, 30, 0, 0.1, 'orange', 'blue', 'red', 'green')
    sphere(draw_balls, -150, -200, 0.1, 'blue', 'gold', 'limegreen', 'white')
    sphere(draw_balls, -60, -80, 0.1, 'red', 'blue', 'gold', 'yellow')
    sphere(draw_balls, -20, 10, 0.05, 'yellow', 'red', 'blue', 'green')

    # рисуем новогоднюю ёлку
    christmas_tree(draw_tree)
    draw_tree.ht()  # скрывает перо, которым рисовали

    # рисуем ещё несколько ёлочных сфер
    sphere(draw_balls, 30, -70, 0.05, 'blue', 'gold', 'limegreen', 'white')
    sphere(draw_balls, -20, 200, 0.1, 'crimson', 'gold', 'limegreen', 'aliceblue')
    sphere(draw_balls, 120, -100, 0.1, 'green', 'gold', 'blue', 'red')
    sphere(draw_balls, -30, 80, 0.1, 'violet', 'red', 'gold', 'green')
    sphere(draw_balls, 30, 150, 0.1, 'yellow', 'red', 'blue', 'green')
    draw_balls.ht()  # скрывает перо, которым рисовали

    # рисуем ещё несколько подарков
    box(draw_gift, 200, -200, 1/5, 'orange', 'blue')
    box(draw_gift, 300, -200, 1/5, 'yellow', 'violet')
    box(draw_gift, 250, -162, 1/10, 'red', 'gold')
    box(draw_gift, 40, -170, 1/12, 'red', 'blue')
    box(draw_gift, -250, -200, 1/4, 'yellow', 'green')
    draw_gift.ht()  # скрывает перо, которым рисовали

    # рисуем снежинку около новогодней ёлки
    to_given_position(draw_snowflake, -300, 0)
    snowflake(draw_snowflake, 55, 4, 'white', 1)
    draw_snowflake.ht()  # скрывает перо, которым рисовали

    # добавляем текст
    draw_text.color('crimson')
    to_given_position(draw_text, -300, 200)
    style = ('Times New Roman', 35, 'normal')
    draw_text.write('Счастливого Нового года \n и Рождества!',
                    font=style, align='center')
    draw_text.ht()  # скрывает перо, которым рисовали

    # cv = turtle.getcanvas()
    # cv.postscript(file='Happy_New_Year.ps', colormode='color')

    # сигнализируем, что рисунок готов
    turtle.done()
