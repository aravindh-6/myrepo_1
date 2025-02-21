def fun():
    print("great")
    age = 34
    if(age>100):
        print("create")
    else:
        print("not to create")
    a = [12,33,44,66]
    for y in a:
        print(y)

    b = ["add","wind","code"]
    it = iter(b)
    print(next(it))
    print(next(it))
    print(next(it))
fun()