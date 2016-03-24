"""
GUI component of Tantrix Solitaire implementation
http://www.jaapsch.net/puzzles/tantrix.htm
"""

import math
import simplegui

# drawing constant

EDGE_LENGTH = 40
HEX_HEIGHT = math.sqrt(3.0) * EDGE_LENGTH
COLOR_DICT = {"B" : "Blue", "R" : "Red", "Y" : "Yellow", "G" : "Green"}


def dist(pt1, pt2):
    """
    Compute Euclidean distance between two points
    """
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)


def make_hexagon(center):
    """
    Build a hexagin with edges of length EDGE_LENGTH with specified center
    """
    hexagon = [[center[0] + EDGE_LENGTH, center[1]],
               [center[0] + 0.5 * EDGE_LENGTH, center[1] + 0.5 * HEX_HEIGHT],
               [center[0] - 0.5 * EDGE_LENGTH, center[1] + 0.5 * HEX_HEIGHT],
               [center[0] - EDGE_LENGTH, center[1]],
               [center[0] - 0.5 * EDGE_LENGTH, center[1] - 0.5 * HEX_HEIGHT],
               [center[0] + 0.5 * EDGE_LENGTH, center[1] - 0.5 * HEX_HEIGHT],
               [center[0] + EDGE_LENGTH, center[1]]]
    return hexagon


class TantrixGUI:
    """
    GUI class for game
    """

    def __init__(self, game):
        """
        Initialize GUI
        """

        self._game = game
        self._tiling_size = self._game.get_tiling_size()
        self.init_grid()

        canvas_width = 2 * EDGE_LENGTH + (3 * self._tiling_size * EDGE_LENGTH / 2)
        canvas_height = (self._tiling_size + 1) * HEX_HEIGHT
        self._frame = simplegui.create_frame("Tantrix Solitaire demo",
                                            canvas_width, canvas_height)
        self._frame.add_button("Is legal?", self.check_legal, 200)
        self._frame.add_button("Yellow loop of length 10?", self.yellow_loop, 200)
        self._frame.add_button("Red loop of length 10?", self.red_loop, 200)
        self._frame.add_button("Blue loop of length 10?", self.blue_loop, 200)
        self._frame.set_draw_handler(self.draw)
        self._frame.set_canvas_background("White")
        self._frame.set_mouseclick_handler(self.click)
        self._frame.set_mousedrag_handler(self.drag)
        self._frame.start()
        self._mouse_drag = False


    def init_grid(self):
        """
        Precompute triangular grid for use in GUI
        """

        self.corners = [[EDGE_LENGTH, 0.5 * HEX_HEIGHT],
                        [EDGE_LENGTH, (self._tiling_size + 0.5) * HEX_HEIGHT],
                        [EDGE_LENGTH + (3 * self._tiling_size * EDGE_LENGTH / 2),
                         0.5 * (self._tiling_size + 1) * HEX_HEIGHT]]

        self.grid_centers = {}
        for index_i in range(self._tiling_size + 1):
            for index_j in range(self._tiling_size + 1 - index_i):
                grid_index = (index_i, index_j, self._tiling_size - (index_i + index_j))
                grid_center = [0, 0]
                for idx in range(3):
                    grid_center[0] += self.corners[idx][0] * float(grid_index[idx]) / self._tiling_size
                    grid_center[1] += self.corners[idx][1] * float(grid_index[idx]) / self._tiling_size
                self.grid_centers[grid_index] = grid_center

    def closest_grid_center(self, pos):
        """
        Compute index for cell that contains pos
        """
        min_distance = float('inf')
        for grid_index in self.grid_centers.keys():
            grid_center = self.grid_centers[grid_index]
            current_distance = dist(pos, grid_center)
            if current_distance < min_distance:
                min_distance = current_distance
                closest_index = grid_index
        return closest_index

    def check_legal(self):
        """
        Button handler to check for legal configuration
        """
        if self._game.is_legal():
            print "Configuration is legal"
        else:
            print "Configuration is illegal"

    def yellow_loop(self):
        """
        Button handler to check for yellow loop
        """
        if not self._game.is_legal():
            print "Configuration is illegal"
        elif self._game.has_loop("Y"):
            print "Configuration has a yellow loop of length 10"
        else:
            print "Configuration does not have a yellow loop of length 10"

    def red_loop(self):
        """
        Button handler to check for red loop
        """
        if not self._game.is_legal():
            print "Configuration is illegal"
        elif self._game.has_loop("R"):
            print "Configuration has a red loop of length 10"
        else:
            print "Configuration does not have a red loop of length 10"

    def blue_loop(self):
        """
        Button handler to check for blue loop
        """
        if not self._game.is_legal():
            print "Configuration is illegal"
        elif self._game.has_loop("B"):
            print "Configuration has a blue loop of length 10"
        else:
            print "Configuration does not have a blue loop of length 10"


    def click(self, pos):
        """
        Mouse click handler, integrated with dragging, fires on mouse up
        """
        up_click_index = self.closest_grid_center(pos)
        if self._mouse_drag and self.current_tile_code:
            if self._game.tile_exists(up_click_index):
                self._game.place_tile(self.down_click_index, self._game.get_code(up_click_index))
            self._game.place_tile(up_click_index, self.current_tile_code)
        elif self._game.tile_exists(up_click_index) and not self._mouse_drag:
            self._game.rotate_tile(up_click_index)
        self._mouse_drag = False



    def drag(self, pos):
        """
        Mouse drag handler, fires on mouse down
        """
        if not self._mouse_drag:
            self.down_click_index = self.closest_grid_center(pos)
            if self._game.tile_exists(self.down_click_index):
                self.current_tile_code = self._game.remove_tile(self.down_click_index)
            else:
                self.current_tile_code = None	# miss the current grab
        self._mouse_drag = True
        self.mouse_position = pos


    def draw_hexagon(self, canvas, center):
        """
        Draw non-fill hexagon on the canvas with given center
        """
        hexagon = make_hexagon(center)
        canvas.draw_polyline(hexagon, 2, "Black")

    def draw_tile(self, canvas, center, code):
        """
        Draw a tile based on its center and code
        Credit to Scott R. for his implementation of circular arcs
        """
        hexagon = make_hexagon(center)
        canvas.draw_polygon(hexagon[:], 2, "White", "Black")

        mid_pts = [[0.5 * (hexagon[idx][dim] + hexagon[idx + 1][dim]) for dim in range(2)]
                   for idx in range(len(hexagon) - 1)]

        for color in COLOR_DICT.keys():
            first = code.find(color)
            second = code.rfind(color)
            arc = (second - first) % 6
            if arc == 3:
                # Straight line across the tile
                canvas.draw_line(mid_pts[first], mid_pts[second], EDGE_LENGTH / 8, COLOR_DICT[color])
            elif arc == 2 or arc == 4:
                # long arc across the tile
                # 60 degree arc centered around the point where the two edges would meet
                src = second
                if arc == 4: src = first

                start_ang = 120 + 60 * src
                offset_ang = (start_ang + 180) * math.pi/180
                #cp = hexagon[src]
                cp = [hexagon[src][0] + EDGE_LENGTH * math.cos(offset_ang), hexagon[src][1] + EDGE_LENGTH * math.sin(offset_ang)]
                rad = EDGE_LENGTH / 2 + EDGE_LENGTH
                pline = []
                for i in range(7):
                    ang = (start_ang + 10 * i) * math.pi/180
                    pt = [cp[0] + rad * math.cos(ang), cp[1] + rad * math.sin(ang)]
                    pline.append(pt)

                canvas.draw_polyline(pline, EDGE_LENGTH / 8, COLOR_DICT[color])
                #canvas.draw_line(mid_pts[first], mid_pts[second], EDGE_LENGTH / 8, COLOR_DICT[color])
            elif arc == 1 or arc == 5:
                # short arc between adjecent edges
                # 120 degree arc, centered around shared corner

                # select edge to sweep in an arc from
                src = second
                if arc == 5: src = first

                # get the rotation point and start angel from src, hexagon, and EDGE_LENGTH
                cp = hexagon[src]
                start_ang = 120 + 60 * src
                rad = EDGE_LENGTH / 2
                pline = []
                for i in range(5):
                    ang = (start_ang + 30 * i) * math.pi/180
                    pt = [cp[0] + rad * math.cos(ang), cp[1] + rad * math.sin(ang)]
                    pline.append(pt)

                canvas.draw_polyline(pline, EDGE_LENGTH / 8, COLOR_DICT[color])

    def draw(self, canvas):
        """
        Draw everything
        """
        for grid_index in self.grid_centers.keys():
            grid_center = self.grid_centers[grid_index]
            if self._game.tile_exists(grid_index):
                self.draw_tile(canvas, grid_center, self._game.get_code(grid_index))
            else:
                self.draw_hexagon(canvas, grid_center)

        if self._mouse_drag and self.current_tile_code:
            self.draw_tile(canvas, self.mouse_position, self.current_tile_code)
