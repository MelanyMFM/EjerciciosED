def encode(a, b, c):
    org = sorted([a, b, c])
    return str(org[0]) + "-" + str(org[1]) + "-" + str(org[-1])


n, t = input().split()
n, t = int(n), int(t)

nums = {}
for i in range(0,n):
    x = int(input())
    nums[i] = x


value_set = set(nums.values())

ya = set()


for i in range(0, n):
    for j in range(i, n):
        if i != j:
            suma = nums[i] + nums[j]
            complemento = t - suma

            if complemento != nums[i] and complemento != nums[j]:
                if complemento in value_set and encode(nums[i], nums[j], complemento) not in ya: #el complemento esta en la lista y no se ha usado

                    temp = encode(nums[i], nums[j], complemento)
                    ya.add(temp)

sorted_set = sorted(ya, key=lambda x: list(map(int, x.split('-'))))

for i in sorted_set:
    print(i[0], i[2], i[-1])

if len(sorted_set) == 0:
    print("")

                
