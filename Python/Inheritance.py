class Car:
    def start():
        print("Engine started")
    
    def stop():
        print("Brakes applied")

class Mustang(Car):
    def set_mode(model):
        self.mode = model

old = Mustang

old.start()
old.stop()
