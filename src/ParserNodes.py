#Node value types
NODE_TYPE_INT = "NODE_TYPE_INT"
NODE_TYPE_FLOAT = "NODE_TYPE_FLOAT"
NODE_TYPE_STR = "NODE_TYPE_STR"
NODE_TYPE_BOOL = "NODE_TYPE_BOOL"
NODE_TYPE_FUNC = "NODE_TYPE_FUNC"
NODE_TYPE_VARIABLE = "NODE_TYPE_VARIABLE"
#=================================
class Node:
    def __init__(self, type : str, value : str) -> None:
        self._type : str = type
        self._value : str = value

    @property
    def value(self):
        return self._value

    """@value.getter
    def value(self): #fix
        global NODE_TYPE_INT
        val = None
        match self._type:
            case NODE_TYPE_INT:
                val = int(self._value)
            case NODE_TYPE_FLOAT:
                val = float(self._value)
            case _:
                pass

        return val"""

    def __repr__(self) -> str:
        return f"({self._type} : {self.value})"
