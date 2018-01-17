def f1(func):
    def run():
        print('时光荏苒，我还是成为了以前的那个人')
        func()
    return run
@f1
def f2():
    print('故事从此再无交集')
f2()
