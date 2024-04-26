import statistics
def getAverage(self):
    return statistics.mean(self)

def getMedian(self):
    return statistics.median(self)

def getMode(self):
    return statistics.mode(self)

scores=[33, 45, 55, 64, 87, 29, 123];
print(getAverage(scores));

print(getMedian(scores));

print(getMode(scores));

