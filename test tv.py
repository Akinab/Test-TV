def details ():
    Description = "Test TV"
    Date = "05-19-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1

    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

    def get_channel(self):
        return self.channel
    
    def get_volume(self):
        return self.volume
    
    
class TestTV:
    def __init__(self):
        self.tv1 = None
        self.tv2 = None

    def create_tvs(self):
        input_text = input("\nEnter 'Test TV' to display tvs: ")
        if input_text == "Test tv":
            self.tv1 = TV()
            self.tv2 = TV()

    def display_tv_info(self):
        if self.tv1 is not None and self.tv2 is not None:
            self.tv1.set_channel(30)
            self.tv1.set_volume(3)
            self.tv2.set_channel(3)
            self.tv2.set_volume(2)

            print("tv1's channel is", self.tv1.get_channel(), "and volume level is", self.tv1.get_volume())
            print("tv2's channel is", self.tv2.get_channel(), "and volume level is", self.tv2.get_volume())


# Create TestTV object and display TV information
test_tv = TestTV()
test_tv.create_tvs()
test_tv.display_tv_info()     