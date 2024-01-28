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
        anniversaries = [year % 100 for year in range(self.year, self.currentYear, 10)
                         if year <= self.currentYear]
        return anniversaries

# task 4
    def modifyYear(self, n: int) -> str:
        year_str = str(self.year)
        first_two_chars = year_str[:2]
        odd_chars = year_str[::2]
        modified_str = first_two_chars * n + odd_chars * n
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
