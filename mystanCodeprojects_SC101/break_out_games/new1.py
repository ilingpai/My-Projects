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
from campy.gui.events.timer import pause
from new2 import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    live_times = NUM_LIVES
    while True:
        # pause
        pause(FRAME_RATE)

        if graphics.ball_falling:
            # update
            graphics.ball.move(graphics.get_vx(), graphics.get_vy())
            graphics.check_for_collisions()

            # Check
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_vx(-graphics.get_vx())
            elif graphics.ball.y <= 0:
                graphics.set_vy(-graphics.get_vy())

            if graphics.ball.y >= graphics.window.height:
                live_times -= 1
                graphics.reset_ball()

            # Stop the game
            if live_times <= 0:
                graphics.window.clear()
                dead = GLabel("GAME")
                dead.font = '-100'
                dead.color = 'black'
                graphics.window.add(dead, x=30, y=200)

                dead = GLabel("OVER")
                dead.font = '-100'
                dead.color = 'black'
                graphics.window.add(dead, x=40, y=400)
            elif graphics.bricks_num == 0:
                graphics.window.clear()
                dead = GLabel("You")
                dead.font = '-100'
                dead.color = 'black'
                graphics.window.add(dead, x=30, y=200)

                dead = GLabel("WIN")
                dead.font = '-100'
                dead.color = 'black'
                graphics.window.add(dead, x=40, y=400)



if __name__ == "__main__":
    main()
