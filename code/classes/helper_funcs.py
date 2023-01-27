def intersect_count(routes, gates):

    # make the coords 3d
    gates_list2d = list(gates.values())
    gates_list = []
    for gate in gates_list2d:
        x, y = gate
        gates_list.append((x, y, 0))

    print(gates_list)
    seen = set()
    intersect_counter = 0
    for route in routes:
        for coord in route:
            if coord not in seen:
                seen.add(coord)
            elif coord not in gates_list:
                intersect_counter += 1

    return intersect_counter
