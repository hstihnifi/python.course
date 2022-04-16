
# Towers Of Hanoi

def hanoi(n, src, dst, tmp):
    i = 1
    if n == 1:
        print(i, "move Disk 1 from source", src, "to destination", dst)
        return

    hanoi(n - 1, src, dst, tmp)
    print(i + 1, "move Disk", n, "from source", src, "to destination", dst)
    hanoi(n - 1, dst, tmp, src)


n = 3
hanoi(n, "A", "c", "B")
