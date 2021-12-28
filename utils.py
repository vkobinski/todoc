class Todo:
    def __init__(self, body):
        self.prefix = body.split(":")[0]
        self.body = body.split(":")[1]
        self.importance = self.prefix.count("O")-1
    def getImportance(self):
        return self.importance
