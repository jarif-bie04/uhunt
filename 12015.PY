t = int(input())

for case in range(t):
    url = dict()

    for _ in range(10):
        key, value = input().strip().split()
        value = int(value)
        url[key] = value
    
    larger = max(url.values())

    print(f"Case #{case+1}:")
    for key, value in url.items():
        if value == larger:
            print(key)