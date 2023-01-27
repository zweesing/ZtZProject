def intersect_count(routes):
    seen = set()
    intersect_counter = 0
    for route in routes:
        for coord in route:
            if coord not in seen:
                seen.add(coord)
            else:
                intersect_counter += 1

    return intersect_counter
