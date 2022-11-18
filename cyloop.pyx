
def run(loop_counter_max: int) -> int:

    cdef unsigned long lcm = loop_counter_max
    cdef unsigned long acc = 0
    cdef unsigned long i = 1

    while i < lcm:
        acc += i
        i += 1

    return acc