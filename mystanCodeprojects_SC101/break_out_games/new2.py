"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a pinball machine.
If the ball hits the paddle, it will bounce.
If it hits the bricks, it will disappear.
If the ball falls without a street, one life point will be deducted.
The game ends by eliminating all the bricks or falling three times.

Hit a brick and add 1 point.
If the game is over, game over will pop up. If all the bricks are destroyed, You win will be displayed.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5
BRICK_WIDTH = 40
BRICK_HEIGHT = 15
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_OFFSET = 50
BALL_RADIUS = 10
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 15
PADDLE_OFFSET = 50
INITIAL_Y_SPEED = 7
MAX_X_SPEED = 5


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width - paddle_width) // 2, y=self.window_height - paddle_offset)

        # Create a ball
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width - self.ball_radius * 2) // 2,
                        y=(self.window_height - self.ball_radius * 2) // 2)

        # Ball movement control
        self.__dx = 0
        self.__dy = 0
        self.ball_falling = False

        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_ball)

        # Draw bricks
        self.bricks_num = brick_rows * brick_cols
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if i < 2:
                    brick.fill_color = 'red'
                elif i < 4:
                    brick.fill_color = 'orange'
                elif i < 6:
                    brick.fill_color = 'yellow'
                elif i < 8:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                x_pixel = j * (brick_width + brick_spacing)
                y_pixel = brick_offset + i * (brick_height + brick_spacing)
                self.window.add(brick, x=x_pixel, y=y_pixel)

    # Create a score label
        self.score = 0
        self.score_label = GLabel('Score==>' + str(self.score))
        self.score_label.font = '-30'
        self.score_label.color = 'red'
        self.window.add(self.score_label, x=0, y=self.window.height)

    def paddle_move(self, mouse):
        if mouse.x < self.paddle.width // 2:
            self.paddle.x = 0
        elif mouse.x > self.window.width - self.paddle.width // 2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width // 2

    def start_ball(self, event):
        if not self.ball_falling:
            self.ball_falling = True
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def check_for_collisions(self):
        for x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                obj = self.window.get_object_at(x, y)
                if obj is not None:
                    if obj == self.paddle:
                        self.__dy = -self.__dy
                    elif obj != self.score_label:
                        self.window.remove(obj)
                        self.update_score()
                        self.bricks_num -= 1
                        self.__dy = -self.__dy
                    return

    def update_score(self):
        self.score += 1
        self.score_label.text = 'Score==>'+str(self.score)

    def reset_ball(self):
        self.ball_falling = False
        self.__dx = 0
        self.__dy = 0
        self.set_ball_position()

    def set_ball_position(self):
        self.ball.x = (self.window_width - self.ball_radius * 2) // 2
        self.ball.y = (self.window_height - self.ball_radius * 2) // 2

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_vx(self, new_vx):
        self.__dx = new_vx

    def set_vy(self, new_vy):
        self.__dy = new_vy
