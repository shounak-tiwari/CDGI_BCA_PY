def funDeco(x):
    def funcDecorators():
        print("function executions")
        x()
        print("decorators ")
        print("Hey guys Good Morning i hope you are doing well ")
    return funcDecorators

@funDeco
def Haye():
    print("You know i'm very beautiful")

Haye()