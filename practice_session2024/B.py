import sys

n = int(input())
current_number = n // 2
start = 1
finish = n
while start < finish - 1:
    print(f"? {current_number}")
    sys.stdout.flush()
    vote = input()
    if vote[0] == 'g':
        finish = current_number
        current_number = start + (finish - start) // 2
    else:
        start = current_number
        current_number = start + (finish - start) // 2
print(f"! {start}")
sys.stdout.flush()
sys.exit(0)