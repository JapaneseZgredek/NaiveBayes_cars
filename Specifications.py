class Specifications:
    def __init__(self, attributes, opinion):
        self.attributes = attributes
        self.opinion = opinion

    def to_string(self):
        print(str(self.attributes) + ' ' + str(self.opinion))

