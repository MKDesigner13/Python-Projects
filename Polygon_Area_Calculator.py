class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        rect_str = f'Rectangle(width={self.width}, height={self.height})'
        return rect_str

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        rect_pic = ''
        if self.width > 50 or self.height > 50:
            rect_pic = 'Too big for picture.'
        else:
            rect_line = f'{"":*^{self.width}}'
            for i in range(self.height):
                rect_pic += rect_line + '\n'
        return rect_pic

    def get_amount_inside(self, shape):
        width_inside = self.width // shape.width
        height_inside = self.height // shape.height
        amount_inside = 0

        if width_inside > 0:
            if height_inside > 0:
                amount_inside = width_inside * height_inside

        return amount_inside

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        square_str = f'Square(side={self.width})'
        return square_str
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side


"""
Example Usage:

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
"""
        
