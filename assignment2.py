import socket
# task 1
class Assignment2:
    def __init__(self, year):
        self.year = year
        self.currentYear = 2022

# task 2
    def tellAge(self, currentYear) -> str:
        age = currentYear - self.year
        return f"Your age is {age}\n"

# task 3
    def listAnniversaries(self):
        anniversaries = []
        diff = self.currentYear - self.year

        for i in range(10, diff + 1, 10):
            anniversaries.append(i)

        return anniversaries

# task 4
    def modifyYear(self, n: int) -> str:
        year_str = str(self.year)
        mod_year = str(self.year * n)  # year * n
        first_two_chars = year_str[:2]
        odd_nums = mod_year[0::2]
        modified_str = first_two_chars * n + odd_nums
        return modified_str

# task 5
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False

        if not string[0].islower() or string[0] not in 'abcdefghijklmnopqrstuvwxyz':
            return False

        count_digits = sum(char.isdigit() for char in string)
        if count_digits != 1:
            return False

        return True

# task 6
    @staticmethod
    def connectTcp(host, port):
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_socket.connect((host, port))
            tcp_socket.close()

            return True

        except Exception as e:
            print(f"Error: {e}")

            return False

        except Exception as e:
            print(f"Error: {e}")

            return False

# test cases
a = Assignment2(1991)
ret = a.listAnniversaries()
print(ret)  # should print [10, 20, 30]

a = Assignment2(1782)
ret = a.modifyYear(3)
print(ret)  # should print 17171754

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)  # should print False

ret = Assignment2.checkGoodString("foobar0more")
print(ret)  # should print True

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
