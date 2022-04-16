
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


#Answer
# 1 move Disk 1 from source A to destination c
# 2 move Disk 2 from source A to destination c
# 1 move Disk 1 from source c to destination B
# 2 move Disk 3 from source A to destination c
# 1 move Disk 1 from source c to destination B
# 2 move Disk 2 from source c to destination B
# 1 move Disk 1 from source B to destination A
