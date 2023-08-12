import time

x = 0;

start = time.time()
for i in range(1, 100001):
    a = x+i
    d = open("data.txt", "r")
    print(a)
end = time.time()

print(f"{end-start:.3f} sec")