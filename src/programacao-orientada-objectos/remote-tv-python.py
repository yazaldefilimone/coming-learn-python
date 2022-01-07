class ControleDeTv:
    def __init__(self, nomeDaTv):
        self.nomeDaTv = nomeDaTv;
        self.channel = 0;


    def nextChannel(self):
        self.channel = self.channel + 1;
        return self.channel;


    def prevChannel(self):
        self.channel = self.channel - 1;
        return self.channel;


    def changeChannel(self, channel):
        self.channel = channel;
        return self.channel;



controleDeTv = ControleDeTv('samsung');

print(controleDeTv.nextChannel());#1

print(controleDeTv.nextChannel());#2

print(controleDeTv.prevChannel());#1

print(controleDeTv.changeChannel(3));#3


