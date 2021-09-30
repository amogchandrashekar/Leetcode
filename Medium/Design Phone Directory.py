class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.available = set(range(maxNumbers))

    def get(self):
        return self.available.pop() if self.available else -1

    def check(self, number):
        return number in self.available

    def release(self, number):
        self.available.add(number)


if __name__ == '__main__':
    phoneDirectory = PhoneDirectory(3)
    print(phoneDirectory.get())
    print(phoneDirectory.get())
    print(phoneDirectory.check(2))
    print(phoneDirectory.get())
    print(phoneDirectory.check(2))
    print(phoneDirectory.release(2))
    print(phoneDirectory.check(2))