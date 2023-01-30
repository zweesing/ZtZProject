from ..classes.pathfinder import Pathfinder
import random


class Pathfind(Pathfinder):
    """
    subclass of pathfinder class. This algorithm uses a sort of greedy algorithm to find the shortest route.
    """

    def __init__(self, start, end, board, size):
        """
        runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            level (int): z coordinate
        """
        super().__init__(start, end, board, size)

    def find(self):
        """
        the algorithm finds the shortest path between two gates by checking the relative position.
        If the path is blocked in one direction, it picks a new direction randomly.
        This new direction could also be up or down to a new layer.

        Returns:
            list with tuples of path taken, total wire count and the board, in that order.
        """
        route = [(self.start_gate_x, self.start_gate_y, 0)]

        wire_count = 0
        current_gate_x = self.start_gate_x
        current_gate_y = self.start_gate_y
        current_gate_z = 0

        random_direction = ["x", "y", "z"]
        random_direction2 = [1, -1]

        while True:
            # start with x coordinate
            while current_gate_x < self.end_gate_x:
                current_gate_x += 1

                # if the new current position has a z coordinate, it should be updated in the route list

                current_position = (current_gate_x, current_gate_y, current_gate_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                    route.append(current_position)
                    wire_count += 1
                    return route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    current_gate_x -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(random_direction)
                    random.shuffle(random_direction2)
                    made_step = False
                    for xyz in random_direction:
                        for left_right in random_direction2:
                            if xyz == "x" and self.is_valid(
                                current_gate_x + left_right,
                                current_gate_y,
                                current_gate_z,
                            ):
                                current_gate_x += left_right
                                made_step = True

                            if xyz == "y" and self.is_valid(
                                current_gate_x,
                                current_gate_y + left_right,
                                current_gate_z,
                            ):
                                current_gate_y += left_right
                                made_step = True

                            if xyz == "z" and self.is_valid(
                                current_gate_x,
                                current_gate_y,
                                current_gate_z + left_right,
                            ):
                                current_gate_z += left_right
                                made_step = True

                            if made_step:
                                break
                        if made_step:
                            break

                    # if random failed too, it has nowhere to go, and crashes and starts over
                    if not made_step:
                        return "crashed"
                    else:
                        current_position = (
                            current_gate_x,
                            current_gate_y,
                            current_gate_z,
                        )

                # append the new current position and update the wire count
                route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

            # second x direction
            while current_gate_x > self.end_gate_x:
                current_gate_x -= 1

                # if the new current position has a z coordinate, it should be updated in the route list

                current_position = (current_gate_x, current_gate_y, current_gate_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                    route.append(current_position)
                    wire_count += 1
                    return route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    current_gate_x += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(random_direction)
                    random.shuffle(random_direction2)
                    made_step = False
                    for xyz in random_direction:
                        for left_right in random_direction2:
                            if xyz == "x" and self.is_valid(
                                current_gate_x + left_right,
                                current_gate_y,
                                current_gate_z,
                            ):
                                current_gate_x += left_right
                                made_step = True

                            elif xyz == "y" and self.is_valid(
                                current_gate_x,
                                current_gate_y + left_right,
                                current_gate_z,
                            ):
                                current_gate_y += left_right
                                made_step = True

                            elif xyz == "z" and self.is_valid(
                                current_gate_x,
                                current_gate_y,
                                current_gate_z + left_right,
                            ):
                                current_gate_z += left_right
                                made_step = True

                            if made_step:
                                break
                        if made_step:
                            break
                    if not made_step:
                        # if rando failed, try an intersection. woof.
                        for xyz in random_direction:
                            for left_right in random_direction2:
                                if xyz == "x" and self.is_valid(
                                    current_gate_x + 2 * left_right,
                                    current_gate_y,
                                    current_gate_z,
                                ):
                                    # make two steps, so add the intersection point manually

                                    current_gate_x += left_right
                                    current_position = (
                                        current_gate_x,
                                        current_gate_y,
                                        current_gate_z,
                                    )
                                    route.append(current_position)
                                    current_gate_x += left_right
                                    made_step = True

                                elif xyz == "y" and self.is_valid(
                                    current_gate_x,
                                    current_gate_y + 2 * left_right,
                                    current_gate_z,
                                ):
                                    current_gate_y += left_right
                                    current_position = (
                                        current_gate_x,
                                        current_gate_y,
                                        current_gate_z,
                                    )
                                    route.append(current_position)
                                    current_gate_y += left_right
                                    made_step = True

                                elif xyz == "z" and self.is_valid(
                                    current_gate_x,
                                    current_gate_y,
                                    current_gate_z + 2 * left_right,
                                ):
                                    current_gate_z += left_right
                                    current_position = (
                                        current_gate_x,
                                        current_gate_y,
                                        current_gate_z,
                                    )
                                    route.append(current_position)
                                    current_gate_z += left_right
                                    made_step = True

                                if made_step:
                                    break
                            if made_step:
                                break

                    # if random failed too, it has nowhere to go, and crashes and starts over
                    if not made_step:
                        return "crashed"
                    else:
                        current_position = (
                            current_gate_x,
                            current_gate_y,
                            current_gate_z,
                        )

                # append the new current position and update the wire count
                route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

            # y direction
            while current_gate_y < self.end_gate_y:
                current_gate_y += 1

                # if the new current position has a z coordinate, it should be updated in the route list

                current_position = (current_gate_x, current_gate_y, current_gate_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                    route.append(current_position)
                    wire_count += 1
                    return route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    current_gate_y -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(random_direction)
                    random.shuffle(random_direction2)
                    made_step = False
                    for xyz in random_direction:
                        for left_right in random_direction2:
                            if xyz == "x" and self.is_valid(
                                current_gate_x + left_right,
                                current_gate_y,
                                current_gate_z,
                            ):
                                current_gate_x += left_right
                                made_step = True

                            if xyz == "y" and self.is_valid(
                                current_gate_x,
                                current_gate_y + left_right,
                                current_gate_z,
                            ):
                                current_gate_y += left_right
                                made_step = True

                            if xyz == "z" and self.is_valid(
                                current_gate_x,
                                current_gate_y,
                                current_gate_z + left_right,
                            ):
                                current_gate_z += left_right
                                made_step = True

                            if made_step:
                                break
                        if made_step:
                            break
                    # if random failed too, it has nowhere to go, and crashes and starts over
                    if not made_step:
                        return "crashed"
                    else:
                        current_position = (
                            current_gate_x,
                            current_gate_y,
                            current_gate_z,
                        )

                # append the new current position and update the wire count
                route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

            # second y direction
            while current_gate_y > self.end_gate_y:
                current_gate_y -= 1

                # if the new current position has a z coordinate, it should be updated in the route list

                current_position = (current_gate_x, current_gate_y, current_gate_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                    route.append(current_position)
                    wire_count += 1
                    return route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    current_gate_y += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(random_direction)
                    random.shuffle(random_direction2)
                    made_step = False
                    for xyz in random_direction:
                        for left_right in random_direction2:
                            if xyz == "x" and self.is_valid(
                                current_gate_x + left_right,
                                current_gate_y,
                                current_gate_z,
                            ):
                                current_gate_x += left_right
                                made_step = True

                            if xyz == "y" and self.is_valid(
                                current_gate_x,
                                current_gate_y + left_right,
                                current_gate_z,
                            ):
                                current_gate_y += left_right
                                made_step = True

                            if xyz == "z" and self.is_valid(
                                current_gate_x,
                                current_gate_y,
                                current_gate_z + left_right,
                            ):
                                current_gate_z += left_right
                                made_step = True

                            if made_step:
                                break
                        if made_step:
                            break

                    # if random failed too, it has nowhere to go, and crashes and starts over
                    if not made_step:
                        return "crashed"
                    else:
                        current_position = (
                            current_gate_x,
                            current_gate_y,
                            current_gate_z,
                        )

                # append the new current position and update the wire count
                route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

            # z positive
            while current_gate_z < 0:
                current_gate_z += 1

                # if the new current position has a z coordinate, it should be updated in the route list

                current_position = (current_gate_x, current_gate_y, current_gate_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                    route.append(current_position)
                    wire_count += 1
                    return route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    current_gate_z -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(random_direction)
                    random.shuffle(random_direction2)
                    made_step = False
                    for xyz in random_direction:
                        for left_right in random_direction2:
                            if xyz == "x" and self.is_valid(
                                current_gate_x + left_right,
                                current_gate_y,
                                current_gate_z,
                            ):
                                current_gate_x += left_right
                                made_step = True

                            if xyz == "y" and self.is_valid(
                                current_gate_x,
                                current_gate_y + left_right,
                                current_gate_z,
                            ):
                                current_gate_y += left_right
                                made_step = True

                            if xyz == "z" and self.is_valid(
                                current_gate_x,
                                current_gate_y,
                                current_gate_z + left_right,
                            ):
                                current_gate_z += left_right
                                made_step = True

                            if made_step:
                                break

                        if made_step:
                            break

                    # if random failed too, it has nowhere to go, and crashes and starts over
                    if not made_step:
                        return "crashed"
                    else:
                        current_position = (
                            current_gate_x,
                            current_gate_y,
                            current_gate_z,
                        )

                # append the new current position and update the wire count
                route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

            # z negative
            while current_gate_z > 0:
                current_gate_z -= 1

                # if the new current position has a z coordinate, it should be updated in the route list

                current_position = (current_gate_x, current_gate_y, current_gate_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                    route.append(current_position)
                    wire_count += 1
                    return route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    current_gate_z += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(random_direction)
                    random.shuffle(random_direction2)
                    made_step = False
                    for xyz in random_direction:
                        for left_right in random_direction2:
                            if xyz == "x" and self.is_valid(
                                current_gate_x + left_right,
                                current_gate_y,
                                current_gate_z,
                            ):
                                current_gate_x += left_right
                                made_step = True

                            if xyz == "y" and self.is_valid(
                                current_gate_x,
                                current_gate_y + left_right,
                                current_gate_z,
                            ):
                                current_gate_y += left_right
                                made_step = True

                            if xyz == "z" and self.is_valid(
                                current_gate_x,
                                current_gate_y,
                                current_gate_z + left_right,
                            ):
                                current_gate_z += left_right
                                made_step = True

                            if made_step:
                                break
                        if made_step:
                            break

                    # if random failed too, it has nowhere to go, and crashes and starts over
                    if not made_step:
                        return "crashed"
                    else:
                        current_position = (
                            current_gate_x,
                            current_gate_y,
                            current_gate_z,
                        )

                # append the new current position and update the wire count
                route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[current_gate_z][current_gate_y][current_gate_x] = "1"
