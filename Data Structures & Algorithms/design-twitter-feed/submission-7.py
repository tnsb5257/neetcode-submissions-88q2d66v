class Twitter:

    def __init__(self):
        self.user_map={}
        self.global_counter=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_data=self.user_map.get(userId,{"tweets":[],"followees":set()})
        if not user_data["tweets"]:
            user_data["tweets"].append((-(self.global_counter+1),tweetId,userId,0))
        else:
            last_index = len(user_data["tweets"])-1
            user_data["tweets"].append((-(self.global_counter+1),tweetId,userId,last_index+1))
        self.global_counter+=1
        self.user_map[userId]=user_data
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_list = []
        if userId not in self.user_map:
            return []
        if self.user_map[userId]["tweets"]:
            tweets_list.append(self.user_map[userId]["tweets"][-1])
        for user in self.user_map[userId]["followees"]:
            if user in self.user_map and self.user_map[user]["tweets"]:
                tweets_list.append(self.user_map[user]["tweets"][-1])
        heapq.heapify(tweets_list)
        news_feed=[]
        k=10
        while tweets_list and k>0:
            k-=1
            time,tweetid,userId,index=heapq.heappop(tweets_list)
            if index > 0:
                heapq.heappush(tweets_list,self.user_map[userId]["tweets"][index-1])
            news_feed.append(tweetid)
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId==followerId:
            return
        user_data=self.user_map.get(followerId,{"tweets":[],"followees":set()})
        user_data["followees"].add(followeeId)
        self.user_map[followerId]=user_data
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId==followerId:
            return
        user_data=self.user_map.get(followerId,{"tweets":[],"followees":set()})
        if followeeId in user_data["followees"]:
            user_data["followees"].remove(followeeId)
            self.user_map[followerId]=user_data
        return