import socket
# task 1
class Assignment2:
    def __init__(self, year: int):
        self.year = year
        self.currentYear = 2022

# task 2
    def tellAge(self, currentYear: int):
        age = currentYear - self.currentYear
        print("Your age is {age}")

# task 3
    def listAnniversaries(self):
        anniversaries = [year for year in range(self.year, self.currentYear, 10)
                         if year + 10 <= self.currentYear]
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
            # Create a TCP IPv4 socket
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the specified host and port
            tcp_socket.connect((host, port))

            # Close the connection
            tcp_socket.close()

            # Return True if the connection was established correctly
            return True

        except Exception as e:
            # Print or log the exception if something goes wrong
            print(f"Error: {e}")
            # Return False if the connection could not be established
            return False