def assertRange(var, min, max, name):
    if var > max or var < min:
        raise Exception("Invalid argument: {name} out of range")


def roundup(arg):
    if arg % 1 >= 0.5:
        return int(arg + 1)
    else:
        return int(arg)


class Time:
    hours, minutes, seconds = 0, 0, 0

    def __init__(self, nhours: int, nminutes: int, nseconds: int):
        assertRange(nhours, 0, 23, "nhours")
        assertRange(nminutes, 0, 59, "nminutes")
        assertRange(nseconds, 0, 59, "nseconds")

        self.hours, self.minutes, self.seconds = nhours, nminutes, nseconds

    def __add__(self, other):
        nseconds = (self.seconds + other.seconds) % 60
        carry = (self.seconds + other.seconds) // 60

        nminutes = (self.minutes + other.minutes + carry) % 60
        carry = (self.minutes + other.minutes + carry) // 60

        nhours = (self.hours + other.hours + carry) % 24

        return Time(nhours, nminutes, nseconds)

    def __sub__(self, other):
        nseconds = (self.seconds - other.seconds) % 60
        carry = 0 if self.seconds >= other.seconds else -1

        nminutes = (self.minutes - other.minutes + carry) % 60
        carry = 0 if self.minutes >= other.minutes - carry else -1

        nhours = (self.hours - other.hours + carry) % 24

        return Time(nhours, nminutes, nseconds)

    def __truediv__(self, other):
        tseconds = 3600 * self.hours + 60 * self.minutes + self.seconds
        tseconds = roundup(tseconds / other)

        nhours = tseconds // 3600
        tseconds = tseconds % 3600

        nminutes = tseconds // 60
        nseconds = tseconds % 60

        return Time(nhours, nminutes, nseconds)

    def __mul__(self, other):
        tseconds = 3600 * self.hours + 60 * self.minutes + self.seconds
        tseconds = roundup((tseconds * other) % (3600 * 60 * 24))

        nhours = tseconds // 3600
        tseconds = tseconds % 3600

        nminutes = tseconds // 60
        nseconds = tseconds % 60

        return Time(nhours, nminutes, nseconds)

    def __str__(self):
        res = ""

        if self.hours < 10:
            res = res + "0"

        res = res + str(self.hours) + ":"

        if self.minutes < 10:
            res = res + "0"

        res = res + str(self.minutes) + ":"

        if self.seconds < 10:
            res = res + "0"

        res = res + str(self.seconds)

        return res

    def __lt__(self, other):

        if self.hours != other.hours:
            return self.hours < other.hours

        if self.minutes != other.minutes:
            return self.minutes < other.minutes

        if self.seconds != other.seconds:
            return self.seconds < other.seconds

        return False

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __le__(self, other):
        return __lt__(self, other) or __eq__(self, other)

    def __gt__(self, other):
        return not __lt__(self, other) and not __eq__(self, other)

    def __ge__(self, other):
        return not __lt__(self, other)

    def __ne__(self, other):
        return not __eq__(self, other)


t1 = tuple(int(word) for word in input().split(":"))
t2 = tuple(int(word) for word in input().split(":"))
t3 = tuple(int(word) for word in input().split(":"))

sent = Time(t1[0], t1[1], t1[2])
stamp = Time(t2[0], t2[1], t2[2])
received = Time(t3[0], t3[1], t3[2])

print(stamp + (received - sent) / 2)
