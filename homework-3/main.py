from src.channel import Channel

if __name__ == '__main__':
    # Create two instances of the class
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Use various magic methods
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 107800
    print(moscowpython - highload)  # -53600
    print(highload - moscowpython)  # 53600
    print(moscowpython > highload)  # False
    print(moscowpython >= highload)  # False
    print(moscowpython < highload)  # True
    print(moscowpython <= highload)  # True
    print(moscowpython == highload)  # False
