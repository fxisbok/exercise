"""
class convert_unit():
    def __init__(self):
        self.result = 0
    def radians(self,i):
        import math
        self.result = i * math.pi/180
        return self.result
    def degree(self,i):
        import math
        self.result = i * 180/math.pi
        return self.result


class inherit_cu(convert_unit):
    def inch(self,i):
        self.result = i*39.37
        return self.result
    def meter(self,i):
        self.result = i/39.37
        return self.result

a = inherit_cu()
print(a.inch(10))
"""

'''
import convert_unit
print(convert_unit.radians(10))
'''

'''
from convert_unit import radians
print(radians(30))
'''

'''
import convert_unit
print(convert_unit.radians(20))
'''

from a.b.c import convert_unit
print(convert_unit(10))