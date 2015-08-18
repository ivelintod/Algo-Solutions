def square_root(number):
    left = 0
    right = number
    mid = (left + right) / 2.0
    while True:
        if abs(mid * mid - number) < 0.00001:
            return mid
        if mid * mid > number:
            right = mid
        elif mid * mid < number:
            left = mid
        mid = (left + right) / 2.0
    return mid

def squareroot(number):
    left = 0
    right = number
    mid = left + ((right - left) / 2.0)
    while True:
        if mid**2 < number:
            left = mid
        if mid**2 > number:
            right = mid
        if abs(mid**2 - number) < 0.00001:
            break
        mid = left + ((right - left) / 2.0)

    point_index = (str(mid)).index('.')
    res = str(mid)[:point_index + 7]
    questioned = int(res[len(res) - 1])
    final = res[:point_index + 5]
    if questioned >= 5:
        final += str(int(res[len(res) - 2]) + 1)

    return final



def main():
    num = int(input())
    print(squareroot(num))


if __name__ == '__main__':
    main()
