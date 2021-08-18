for K in range(1,10):
    suffix = "лет"
    if (K//10)%10 != 1:
        if K%10 == 1:
            suffix = "год"
        elif K%10 in (2,3,4):
            suffix = "года"
    print("Мне", K, suffix)