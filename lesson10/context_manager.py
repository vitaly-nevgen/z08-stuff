class MyContextManager:
    def __enter__(self):
        print('I have entered')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('I have exited:', exc_type, exc_val)


with MyContextManager():
    print('Hello!')