#!/usr/bin/python3
for out in range(10):
    for inr in range(out + 1, 10):
        if out == inr:
            continue
        if inr == 9 and out == 8:
            print(f"{out}{inr}")
            break
        print(f"{out}{inr}, ", end="")

