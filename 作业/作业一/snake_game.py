import turtle
import time
import random

# 游戏窗口设置
window = turtle.Screen()
window.title("贪吃蛇")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# 蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 计分板
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("得分: 0", align="center", font=("Arial", 24, "normal"))

segments = []

# 方向控制函数
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# 键盘绑定
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

# 移动函数
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 主游戏循环
while True:
    window.update()
    
    # 边界碰撞检测
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # 清除蛇身
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write("得分: {}".format(score), align="center", font=("Arial", 24, "normal"))
    
    # 吃到食物
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # 增加蛇身
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # 增加得分
        score += 10
        score_display.clear()
        score_display.write("得分: {}".format(score), align="center", font=("Arial", 24, "normal"))
    
    # 移动蛇身
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # 自碰撞检测
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            score_display.clear()
            score_display.write("得分: {}".format(score), align="center", font=("Arial", 24, "normal"))
    
    time.sleep(0.1)

window.mainloop()