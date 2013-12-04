import random

class Room(object):
    """Represents a room in a map grid"""

    def __init__ (self, w=10, h=10):
        self.w = w
        self.h = h

    def __str__ (self):
        return 'Room object with bottom left corner at %d,%d, width %d, and height %d' % (self.x, self.y, self.w, self.h)


class Map(object):
    """Represents a map in points"""
    

    def __getitem__ (self, key):
        ####THIS DOES NOT WORK YET. NEED TO MAKE __getitem__ AND __setitem__.

    def __init__ (self, w=100, h=100):
        for x in range(w):
            for y in range(h):
                self[x][y].blocked = True
        self.w = w
        self.h = h

    def __str__ (self):
        """prints graphical representation of map"""
        d=dict()
        for y in range(self.h):
            print ''
            for x in range(self.w):
                if map[x][y].blocked:
                    print 'x'
                else:
                    print ' '
    
# connecting every room to each other with tunnels
# combination of v and h tunnels for connection
   def horizonta_tunnel(x1,x2,y):
       for x in range (min(x1,x2), max(x1,x2)+1):
           map[x][y].blocked = False 
           # block_sight tells if the tile will block line of sight for players/monsters
           map[x][y].block_sight = False 
           
   def vertical_tunnel(y1,y2,x):
       for y in range(min(y1,y2),max(y1,y2)+1):
           map[x][y].blocked = False 
           map[x][y].block_sight = False 


def generate_position(room, map):
    """Generates x and y position for bottom left corner of room"""
    x_pos=random.randint(0, map.w-room.w)
    y_pos=random.randint(0, map.h-room.h)

    for i in range(room.w):
        for j in range(room.h):
            if not h[x_pos + i][y_pos + j]:
                return generate_position(room,map)
    return (x_pos,y_pos)
    

def main():
    maps=Map()
    print maps
    
if __name__ == '__main__':
    main()