import random

def draw_numbers():
    numbers = list(range(1, 17))
    random.shuffle(numbers)
    return numbers

if __name__ == "__main__":
    drawn_numbers = draw_numbers()
    print("Numbers drawn in random order:", drawn_numbers)


# [4, 15, 7, 11, 16, 12, 13, 8, 14, 6, 3, 5, 9, 1, 10, 2]