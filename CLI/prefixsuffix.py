# Previous Method
'''
def remove_suffix2(input_string: str, suffix: str) -> str:
    if suffix and input_string.endswith(suffix):
        return input_string[: -len(suffix)]
    return input_string


def remove_prefix2(input_string: str, prefix: str) -> str:
    if prefix and input_string.startswith(prefix):
        return input_string[len(prefix):]
    return input_string
'''

# New Method using classes


class myString:
    def __init__(self, strcon):
        self.stringContent = strcon

    def __repr__(self):
        return self.stringContent

    def test(self):
        print("prueba: " + self.stringContent)

    def remove_prefix(self, myPrefix):
        self.stringContent = self.stringContent[len(myPrefix):]
        return self

    def remove_suffix(self, mySuffix):
        self.stringContent = self.stringContent[:-len(mySuffix)]
        return self
