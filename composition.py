
class Processor:
    def __init__(self,model,clock_speed):
        self.model = model
        self.clock_speed = clock_speed

class computer:
    def __init__(self,processor):
        self.processor = processor

    def get_info(self):
        print(self.processor.model,self.processor.clock_speed)

intel = Processor('i4','5000hz')
dummy = computer(intel)
dummy.get_info()

