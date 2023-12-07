
DELETED = "DELETED"


def h(x, M):
    return x % M


def insert(x, H, M):
    i = h(x, M)
    while H[i] is not None:
        i = (i + 1) % M
    H[i] = x


def search(x, H, M):
    i = h(x, M)  # Assuming h(x) = x mod M as mentioned in your description
    while H[i] is not None:
        if H[i] == x:
            return H[i]  # Return the value if found
        i = (i + 1) % M
    return None  # Return None if the element is not found


def eagerDelete(x, H, M):
    i = h(x, M)
    while H[i] is not None:
        if H[i] == x:
            # Perform eager deletion
            H[i] = None
            shift_position = i
            next_position = (i + 1) % M

            while H[next_position] is not None:
                if h(H[next_position], M) <= i:
                    H[shift_position] = H[next_position]
                    shift_position = next_position
                next_position = (next_position + 1) % M

            H[shift_position] = None
            return

        i = (i + 1) % M


def lazyDelete(x, H, M):
    i = h(x, M)
    while H[i] is not None:
        if H[i] == x:
            H[i] = DELETED
            return
        i = (i + 1) % M


def insertV2(x, H, M):
    i = h(x, M)
    while H[i] is not None and H[i] != DELETED:
        i = (i + 1) % M
    H[i] = x


def searchV2(x, H, M):
    i = h(x, M)
    while H[i] is not None:
        if H[i] == x:
            return H[i]
        i = (i + 1) % M
    return None


