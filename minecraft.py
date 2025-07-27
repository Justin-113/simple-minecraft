class Block:
    def __init__(self, x, y):
        self.name = "Default Block"
        self.symbol = "B"
        self.durability = 0
        self.x = x
        self.y = y

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_durability(self):
        return self.durability

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_broken(self):
        return self.durability <= 0

    def reduce_durability(self):
        if self.is_broken():
            return
        self.durability -= 1

    def __str__(self):
        return self.symbol


class Grass(Block):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.name = "Grass"
        self.symbol = "~~~"
        self.durability = 1



class Stone(Block):
    def __init__(self,x, y):
        super().__init__(x,y)
        self.name = "Stone"
        self.symbol = "^^^"
        self.durability = 2


class Iron(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Iron"
        self.symbol = "(-)"
        self.durability = 5


class BedRock(Block):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.name = "BedRock"
        self.symbol = "###"
        self.durability = 10

    def reduce_durability(self):
        self.durability -= 0


class Player:
    def __init__(self, x, y):
        self.symbol = "^o^"
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move_up(self):
        self.y -= 1
        if self.y < 0:
            self.y = 4

    def move_down(self):
        self.y += 1
        if self.y > 4:
            self.y = 0


    def move_left(self):
        self.x -= 1
        if self.x < 0:
            self.x = 4

    def move_right(self):
        self.x += 1
        if self.x > 4:
            self.x = 0




class Map:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(None)
            self.grid.append(row)
        self.player = Player(-1,-1)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def place_block(self, x, y, block):
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.grid[y][x] != None:
                return False
            self.grid[y][x] = block
            return True
        return False

    def set_player_position(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.grid[y][x] != None:
                return False
            self.player.set_x(x)
            self.player.set_y(y)
            return True
        return False

    def print_map_header(self):
        """Print the map header"""
        total_width = self.width * 6 + 1
        title = " M I N E C R A F T "
        padding = (total_width - len(title) - 2) // 2
        print("+" + " " * padding + title + " " * (total_width - padding - len(title) - 2) + "+")

    def print_map_line(self):
        """Print a horizontal line separator"""
        print("+", end="")
        for _ in range(self.width):
            print("-----+", end="")
        print()

    def print_tile_spacer(self):
        """Print a row of empty spaces between tiles"""
        print("+", end="")
        for _ in range(self.width):
            print("     +", end="")
        print()

    def print_map(self):
        """Print the entire map with tiles and borders"""
        self.print_map_line()
        self.print_map_header()
        self.print_map_line()

        for y in range(self.height):
            print("+", end="")
            for x in range(self.width):
                print("     +", end="")

            row_string = "\n  "

            for x in range(self.width):
                if x == self.player.get_x() and y == self.player.get_y():
                    row_string += "^o^"
                elif self.grid[y][x] is not None:
                    row_string += self.grid[y][x].get_symbol()
                else:
                    row_string += "   "

                if x < self.width - 1:
                    row_string += "   "

            print(row_string)


        self.print_tile_spacer()
        self.print_map_line()

    def move_player(self,direction):
        x_before_move = self.player.get_x()
        y_before_move = self.player.get_y()
        if direction == "w":
            self.player.move_up()
            print("Move up")
        elif direction == "a":
            self.player.move_left()
            print("Move left")
        elif direction == "s":
            self.player.move_down()
            print("Move down")
        elif direction == "d":
            self.player.move_right()
            print("Move right")

        x_after_move = self.player.get_x()
        y_after_move = self.player.get_y()
        if self.find_block_by_position(x_after_move, y_after_move) is not None:
            if self.find_block_by_position(x_after_move, y_after_move).get_name() == "Stone" or self.find_block_by_position(x_after_move, y_after_move).get_name() == "Iron":
                map.set_player_position(x_before_move,y_before_move)

    def find_block_by_position(self, x, y):
        block = self.grid[y][x]
        return block

    def find_block_by_direction(self, direction):
        player_x = self.player.get_x()
        player_y = self.player.get_y()
        block = None
        if direction == "w":
            if player_y == 0:
                print("invalid")
                return None
            block = self.find_block_by_position(player_x, player_y - 1)

        elif direction == "a":
            if player_x == 0:
                print("invalid")
                return None
            block = self.find_block_by_position(player_x - 1, player_y)

        elif direction == "s":
            if player_y == 4:
                print("invalid")
                return None
            block = self.find_block_by_position(player_x, player_y + 1)

        elif direction == "d":
            if player_x == 4:
                print("invalid")
                return None
            block = self.find_block_by_position(player_x + 1, player_y)
        return block


if __name__ == "__main__":
    map = Map()
    map.print_map()

    while True:
        print("Please choose the block you want to place in map:")
        print("1. Grass")
        print("2. Stone")
        print("3. Iron")
        choice = int(input())
        position = input("please enter row and column you want to place: ")
        parts = position.split(" ")
        row = int(parts[0])
        col = int(parts[1])
        if choice == 1:
            block = Grass(col,row)
        elif choice == 2:
            block = Stone(col,row)
        elif choice == 3:
            block = Iron(col,row)
        is_placed = map.place_block(col,row,block)
        if is_placed == False:
            print("This position is filled.")
        map.print_map()
        answer = input("Do you want to continue to place block?(y/n) ")
        if answer == "y":
            continue
        elif answer == "n":
            break

    is_set = False
    while is_set == False:
        player_position = input("please enter player position: ")
        player_parts = player_position.split(" ")
        player_row = int(player_parts[0])
        player_col = int(player_parts[1])
        is_set = map.set_player_position(player_col, player_row)
        if is_set == False:
            print("This position is occupied.")

    map.print_map()

    while True:
        direction = input("Please input direction(w/a/s/d/b): ")
        if direction == "w" or direction == "a" or direction == "s" or direction == "d":
            map.move_player(direction)
            map.print_map()
        elif direction == "b":
            break_direction = input("Please input break direction(w/a/s/d): ")
            block_to_break = map.find_block_by_direction(break_direction)
            if block_to_break is not None:
                block_to_break.reduce_durability()
                if block_to_break.is_broken():
                    map.grid[block_to_break.get_y()][block_to_break.get_x()] = None
                    map.print_map()
