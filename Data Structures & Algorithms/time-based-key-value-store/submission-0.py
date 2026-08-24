class TimeMap:

    def __init__(self):
        self.keyvalue = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyvalue:
            self.keyvalue[key] = []
        self.keyvalue[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyvalue.get(key,[])
        res = ""
        left,right = 0, len(values)-1
        while left<=right:
            mid = left+(right-left)//2
            if values[mid][0]<=timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res