
class Parsing:

    def __init__(self, promt:str):
        self.promt = promt
        self.cmds = promt.split(" ")

    def cmdSwitch(self):
        if self.cmds[0] == "/join" and self.cmds[1]:
            return {'cmd' : self.cmds[0], 'room' : self.cmds[1]}
        if self.cmds[0] == "/msg" and self.cmds[1]:
            return {'cmd' : self.cmds[0], 'room' : self.cmds[1], 'msg' : self.cmds[2]}
        return None