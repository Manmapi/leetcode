class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def handle_time(time):
            hour, minute = time.split(":")
            return int(hour) * 60 + int(minute)
        keyTime = [handle_time(x) for x in keyTime]
        record = sorted(zip(keyName, keyTime), key=lambda x: x[1])
        tracker = defaultdict(deque)
        result = set()
        for name, time in record:
            if name in result:
                continue
            if len(tracker[name]) < 2:
                tracker[name].append(time)
            else:
                if time - tracker[name][0] <= 60:
                    result.add(name)
                else:
                    tracker[name].popleft()
                    tracker[name].append(time)
        return sorted(list(result))
        