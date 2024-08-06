from platform import platform as JD
from platform import machine
from platform import processor
from platform import system
import platform
print(len(platform.python_version_tuple()))


print(system())
print(JD())
print(JD(1))
print(JD(0, 1))


print(processor())


print(machine())