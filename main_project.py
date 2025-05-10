import turtle

# ----- Setup -----
screen = turtle.Screen()
screen.title("PWM Signal Visualizer")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

# ----- Function to Draw PWM Wave -----


def draw_pwm_waveform(duty_cycle, periods=5, total_width=500):
    pen.penup()
    pen.goto(-total_width // 2, 0)
    pen.pendown()

    unit_width = total_width // periods
    high_time = unit_width * (duty_cycle / 100)
    low_time = unit_width - high_time

    for _ in range(periods):
        # HIGH signal (Green Line)
        pen.color("green")
        pen.forward(high_time)
        pen.right(90)
        pen.forward(50)
        pen.left(90)

        # LOW signal (Red Line)
        pen.color("red")
        pen.forward(low_time)
        pen.left(90)
        pen.forward(50)
        pen.right(90)

    pen.hideturtle()

# ----- Get User Input -----
while True:
    try:
        duty = float(input("Enter Duty Cycle (0 to 100): "))
        if 0 <= duty <= 100:
            break
        else:
            print("Please enter a valid number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ----- Draw the Wave -----
draw_pwm_waveform(duty_cycle=duty)

# ----- Exit on Click -----
screen.exitonclick()
