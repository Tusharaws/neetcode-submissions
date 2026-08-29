class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp,tweetId))
        self.timestamp += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        followes = self.following[userId] | {userId}
        for follwe_id in followes:
            user_tweets = self.tweets[follwe_id]
            for i in range(1,min(10,len(user_tweets))+1):
                timestamp, tweetId = user_tweets[-i]
                heapq.heappush(min_heap,(timestamp,tweetId))
                if len(min_heap)>10:
                    heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
