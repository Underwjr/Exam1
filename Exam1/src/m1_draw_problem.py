###############################################################################
#   You are going to do a great job on this exam!
#   Read each question carefully.
#   Be sure to commit and push after each question
#   Be sure to right-click on src, and Mark Directory as Sources root
#   You will be asked to write 3 functions that demonstrate your
#   understanding of the concepts covered in class
#
###############################################################################
import rosegraphics as rg


def main():
    #
    #   Tests are called from here.  Do not make any changes to main
    #
    test_draw_a_picture()



def test_draw_a_picture():
    ###############################################################################
    #   This method tests draw_a_picture
    #
    ###############################################################################
    point1 = rg.Point(100, 100)
    n = 10
    test_window = rg.RoseWindow(500, 500)

    #  tests draw_a_picture with point 1, n=10, and test_window
    print('###################################################')
    print('Test 1 of draw_a_picture.')
    print('Called with point1 =', point1)
    print( 'n =', n, ' color = blue')
    print('###################################################')
    draw_a_picture(point1, n, 'blue', test_window)

    point2 = rg.Point(100, 300)
    n = 4
    #  tests draw_a_picture with point 2, n =4, test_window
    print('###################################################')
    print('Test 2 of draw_a_picture.')
    print('Called with point2 =', point2)
    print( 'n =', n, ' color = green')
    print('###################################################')
    draw_a_picture(point2, n, 'green', test_window)
    test_window.close_on_mouse_click()

###############################################################################
# def draw_a_picture(point, n, color, window):
#     """
#     See   m1_draw_problem_picture.pdf   in this project for pictures
#     that may help you better understand the following specification:
#
#     What comes in:
#       -- An rg.Point.
#       -- A positive integer n.
#       -- A fill-color
#       -- An rg.RoseWindow.
#
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#       Draws an rg.Circle with the given point as the center.
#       The color is used as the fill-color of the circle
#       The circle has a radius of 50 pixels
#       The program draws n additional rg.Circles
#       on the given rg.RoseWindow such that:
#       -- The center of the leftmost circle is at the given point
#          Each new circle has a center located 25 pixels to the right
#          and 15 pixels down from the center of the last circle
#          This should form a "diagonal line" of circles
#          The test calls have been written for you in main
#       -- There is a 0.5 second pause after each rg.Circle is drawn.
#       Must  ** NOT close **   the window.
#
#     Type hints:
#       :type circle: rg.Circle
#       :type n: int
#       :type window: rg.RoseWindow
#     """
# -------------------------------------------------------------------------
#  TODO: 1. Implement and test the draw_a_picture function.
#           Tests have been written for you (above in main).
#  We suggest breaking this into multiple commits.
#     Can you show the right circle?
#     Can you make the right number of circles?
#     Are they in the right location?
#     Can you make it display the right color?
############################################################################
# HINT:   render(0.5)
#         renders with a half-second pause after rendering.
############################################################################
# -------------------------------------------------------------------------
#
#

def draw_row_of_circles(n, starting_point, color, window):
    """
    What comes in:  The four arguments are:
      -- A positive integer n.
      -- An rg.Point.
      -- A color appropriate for rosegraphics (e.g. 'red')
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws  n  rg.Circle objects in a row,
      all on the given rg.RoseWindow, such that:
        -- The first rg.Circle is centered at the given starting_point.
        -- Each rg.Circle just touches the previous one (to its left).
        -- Each rg.Circle has radius 20.
        -- Each rg.Circle is filled with the given color.
      Must  ** render **     but   ** NOT close **   the rg.RoseWindow.

     Type hints:
      :type n:               int
      :type starting_point:  rg.Point
      :type color:           str
      :type window:          rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # The example below shows one way to solve problems using
    #   HELPER variables (aka AUXILIARY variables)
    # In this approach:
    #  1. You determine all the variables that you need
    #       to construct/draw whatever the problem calls for.
    #       We call these HELPER variables.
    #  2. You initialize them BEFORE the loop, choosing values that
    #       make them just right for constructing and drawing the
    #       FIRST object to be drawn, in the FIRST time through the loop.
    #       For example,   x = starting_point.x   in the example below.
    #  3. You determine how many times the loop should run
    #       (generally, however many objects you want to draw)
    #       and write the FOR statement for the loop.
    #       For example,    for _ in range(n):  in the example below.
    #  4. Inside the loop you write the statements to construct and
    #       draw the FIRST object to be drawn, using your helper
    #       variables.  This is easy because you chose just the right
    #       values for those helper variables for this FIRST object.
    #  5. Test: Make sure the FIRST object appears.
    #       (It will be redrawn many times, that is OK).
    #  6. Add code at the BOTTOM of the loop that changes the helper
    #       variables appropriately for the NEXT time through the loop.
    #       For example,   x = x + diameter   in the example below.
    #  7. Test and fix as needed.
    #
    # Many students (and professionals) find this technique less
    # error-prone that using the loop variable to do all the work.
    # -------------------------------------------------------------------------

    radius = 20
    diameter = 2 * radius

    x = starting_point.x  # Initialize x and y BEFORE the loop.  Choose ...
    y = starting_point.y  # ... values that make the FIRST object easy to draw.

    for _ in range(n):  # Loop that does NOT use its index variable

        # ---------------------------------------------------------------------
        # Construct the relevant object(s),
        # based on the current x, y and other variables.
        # ---------------------------------------------------------------------
        center = rg.Point(x, y)
        circle = rg.Circle(center, radius)
        circle.fill_color = color

        # Attach the object(s) to the window.
        circle.attach_to(window)

        # ---------------------------------------------------------------------
        # Increment x (and in other problems, other variables)
        # for the thing(s) to draw in the NEXT iteration of the loop.
        # ---------------------------------------------------------------------
        x = x + diameter

    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
def draw_a_picture(point, n, color, window):
    radius = 20
    diameter = 2 * radius

    x = n.x
    y = n.y

    for _ in range(point):

        center = rg.Point(x, y)
        circle = rg.Circle(center, radius)
        circle.fill_color = color

        circle.attach_to(window)

        x = x + diameter

    window.render()

    return


main()
