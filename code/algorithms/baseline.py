from ..classes.pathfinder import Pathfinder
import random 

# Random algoritme maken die een random kant kiest om op te gaan

class Pathfind(Pathfinder):
    def __init__(self, start, end, board):
        super().__init__(start, end, board)

    def findrandom(self):
        route = [(self.start_gate_x, self.start_gate_y)]
        wire_count = 0
        current_gate_x = self.start_gate_x
        current_gate_y = self.start_gate_y
        end_gate = [(self.end_gate_x, self.end_gate_y)]

        while True:
            # hier moet hij dus een random kant kiezen om op te gaan

            # maak een lijst aan met x en y
            random_direction = [current_gate_x, current_gate_y]

            # maak een lijst aan met 1 en -1 (of hij naar links, rechts of boven of beneden moet)
            random_direction2 = [1, -1]

            # kies random uit x of y
            current_gate_x_or_y = random.choice(random_direction)

            # kies random -1 of 1
            left_or_right = random.choice(random_direction2)

            # hier heeft hij dus random uitgekozen of hij naar x of y gaat en of hij plus 1 of min 1 doet. 
            # Hier wordt dat geimplementeerd. 
            current_gate_x_or_y += left_or_right

            # na de random kant gekozen te hebben veranderd de current position hier
            current_position = (current_gate_x, current_gate_y)

            # als hij bij de gate is moet hij wel nog stoppen
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break

            # Als de kant die hij kiest niet valid is moet hij wel nog een andere kant op. 
            # Deze nieuwe kant moet dan ook random zijn.
            # Dit moet hij blijven doen tot hij een positie vindt die wel valid is. Daarom dus een while loop.
            while not self.is_valid(current_position):

                    # Als hij niet de juiste kant op is gegaan moet hij dus terug op de juiste random as. 
                    # We weten welke as dit is omdat we het hebben opgeslagen in current_gate_x_or_y.
                    # Door daarna left_or_right om te draaien kunnen we dus een stap terug.
                    current_gate_x_or_y += (-1 * left_or_right)

                    # Daarna moet hij weer een random kant kiezen om op te gaan. 
                    # Dit gaan we op dezelfde manier doen als dat we de eerste keer een random kant hebben gekozen.
                    # kies random uit x of y
                    current_gate_x_or_y = random.choice(random_direction)

                    # kies random -1 of 1
                    left_or_right = random.choice(random_direction2)

                    # hier heeft hij dus random uitgekozen of hij naar x of y gaat en of hij plus 1 of min 1 doet. 
                    # Hier wordt dat geimplementeerd. 
                    current_gate_x_or_y += left_or_right

                    current_position = (current_gate_x, current_gate_y)

            route.append(current_position)
            wire_count += 1
            self.board[current_gate_y][current_gate_x] = "1"