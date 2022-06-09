d = {"a": 1, "b": 2, "c": 3}
for i in range(3):
    try:
        v = int(input("Enter number: "))
        print(v)
        k = input("Enter key to search: ")
        print(d[k])
        break
    except ValueError as e:
        print("Entered Wrong input | ", e)
    except KeyError as e:
        print("Entered Wrong Key | ", e)
else:
    print("your attempts are over, pls contact class teacher")
