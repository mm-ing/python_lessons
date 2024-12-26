import math

class Draw:
    def __init__(self, canvas):
        self.canvas = canvas
        self.outline_color = 'blue'
        self.fill_color = 'yellow'
        self.line_width = 3
        pass

    def update(self):
        self.canvas.pack()
        self.canvas.update()

    def delete_object(self, object):
        self.canvas.delete(object)
    
    def create_line(self, x1, y1, x2, y2, line_width=3, color='blue'):
        line = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=line_width)
        return line
    
    def create_polyline(self, points, line_width=3, color='blue'):
        polyline = self.canvas.create_line(points, fill=color, width=line_width)
        return polyline

    def create_circle(self, center_x, center_y, radius, line_width=3, outline_color='blue', fill_color='red'):  
        x, y = center_x, center_y
        r = radius
        circle = self.canvas.create_oval(x-r, y-r, x+r, y+r, outline=outline_color, fill=fill_color, width=line_width)
        return circle

    def create_rectangle(self, x1, y1, x2, y2, line_width=3, outline_color='blue', fill_color='yellow'):
        rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, outline=outline_color, fill=fill_color, width=line_width)
        return rectangle

    def create_text(self, x, y, text, color='blue'):
        text = self.canvas.create_text(x, y, text=text, fill=color)
        return text

    def create_polygon(self, x1, y1, x2, y2, x3, y3, line_width=3, outline_color='blue', fill_color='red'):
        polygon = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline=outline_color, fill=fill_color, width=line_width)
        return polygon

    def create_arc(self, x1, y1, x2, y2, start, extent, line_width=3, outline_color='blue', fill_color='yellow'):
        arc = self.canvas.create_arc(x1, y1, x2, y2, start=start, extent=extent, outline=outline_color, fill=fill_color, width=line_width)
        return arc

    def create_oval(self, x1, y1, x2, y2, line_width=3, outline_color='blue', fill_color='yellow'):
        oval = self.canvas.create_oval(x1, y1, x2, y2, outline=outline_color, fill=fill_color, width=line_width)
        return oval
    
    # create rotated line
    def create_rotated_line(self, angle_in_degrees, line_length, center_x, center_y):
        start_end_x_y = []
        angle_in_radians = angle_in_degrees * math.pi / 180
        # delta x y
        delta_x = line_length * math.cos(angle_in_radians)
        delta_y = line_length * math.sin(angle_in_radians)
        #start point
        start_x = center_x - delta_x
        start_y = center_y - delta_y
        start_end_x_y.append(start_x)
        start_end_x_y.append(start_y)
        #end point
        end_x = center_x + delta_x
        end_y = center_y + delta_y
        start_end_x_y.append(end_x)
        start_end_x_y.append(end_y)
        # create line
        rotatedline = self.create_line(start_end_x_y[0], start_end_x_y[1], start_end_x_y[2], start_end_x_y[3])  
        return rotatedline
    
    # create orthgonal lines from a list of lines
    def create_ortho_lines(self, line_def, line_length, x, y):        
        # create coordinates
        points = self.__convert_line_definitions_to_points(line_def, line_length, x, y)

        # create lines
        geometry = self.create_polyline(points)
  
        return geometry
    
    # convert line definitions to points
    def __convert_line_definitions_to_points(self, line_def, line_length, start_x, start_y):        
        points = [start_x, start_y]
        e_x = start_x
        e_y = start_y

        for line in line_def:
            if line[0] == 'v':
                e_y = e_y + line_length * line[1]
            if line[0] == 'h':
                e_x = e_x + line_length * line[1]
            if line[0] == 'vh':
                e_x = e_x + line_length * line[1]
                e_y = e_y + line_length * line[1]
            points.append(e_x)
            points.append(e_y)

        return points

