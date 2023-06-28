requests = int(input())

registration = {}
for i in range(requests):
    name = input()
    if not name in registration:
        registration[name] = [name+"0"]
        print("OK")
    else:
        last_num = int(registration[name][-1][len(name):])
        registration[name].append(name+str(last_num+1))
        print(registration[name][-1])
        #lol