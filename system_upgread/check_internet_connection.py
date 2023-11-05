import socket
import time


class CheckInternetConnection:

    def is_internet_connected(self):
        try:
            # Attempt to create a socket connection to Google's public DNS server
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            pass
        return False

    def connection_available(self):

        # Check internet connection
        if self.is_internet_connected():
            print("Internet connection is available.")
            return "connected"
        else:
            print("No internet connection.")
            return "no connected"

    def try_until_connect(self):
        internet_connection = False
        while internet_connection is False:
            if self.connection_available() == "connected":
                internet_connection = True
                # print("continuing")
            else:
                time.sleep(4)
                self.connection_available()


if __name__ == "__main__":
    CheckInternetConnection().try_until_connect()
