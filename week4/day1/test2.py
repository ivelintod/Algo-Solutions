class maikati:

    a = [4]


def main():
    k = maikati()
    m = maikati()
    k.a.append(5)
    m.a.append(6)
    print(k.a)
    print(m.a)
    lq = [2, 5, 4]
    print(tuple(lq))

if __name__ == '__main__':
    main()
