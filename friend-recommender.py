#!/usr/bin/env python3

class SocialNetwork:

    def __init__(self):
        '''Constructor; initialize an empty social network
        '''
        #Makes social network using dictionary
        self.users = {}

    def list_users(self):
        '''List all users in the network

        Returns:
            [str]: A list of usernames
        '''
        return list(self.users.keys())

    def add_user(self, user):
        '''Add a user to the network

        This user will have no friends initially.

        Arguments:
            user (str): The username of the new user

        Returns:
            None
        '''
        self.users[user] = []

    def add_friend(self, user, friend):
        '''Adds a friend to a user

        Note that "friends" are one-directional - this is the equivalent of
        "following" someone.

        If either the user or the friend is not a user in the network, they
        should be added to the network.

        Arguments:
            user (str): The username of the follower
            friend (str): The username of the user being followed

        Returns:
            None
        '''
        #Checks if user and friend are already in network, if not, they are added
        if user not in self.users:
            self.users[users] = []
        if friend not in self.users:
            self.users[friend] = []
        #Adding friend to user's values
        self.users[user].append(friend)

    def get_friends(self, user):
        '''Get the friends of a user

        Arguments:
            user (str): The username of the user whose friends to return

        Returns:
            [str]: The list of usernames of the user's friends

        '''
        return self.users[user]

    def suggest_friend(self, user):
        '''Suggest a friend to the user

        See project specifications for details on this algorithm.

        Arguments:
            user (str): The username of the user to find a friend for

        Returns:
            str: The username of a new candidate friend for the user
        '''

        #Finding the most similar user in the network with Jaccard index
        jaccard = {}
        for people, friends in self.users.items():
            if people != user:
                #Finds number of similar followers
                comparing_followers = len(set(self.users[user]).intersection(set(friends)))
                #Finds total number of followers together
                total_together = len(set(self.users[user])).union(set(friends))
                #Calculates jaccard index
                jaccard[people] = comparing_followers / total_together
            #Finds most similar follower by finding user with highest jaccard index in dictionary
            most_similar = max(jaccard, key = jaccard.get)

        #Finding the user's friend with most followers that current user doesn't already follow
        most_followed_friend = {}
        for person in self.users[most_similar]:
            if person not in self.users[user]:
                most_followed_friend[person] = len(self.users[person])
        #Returns most followed friend by finding user with the most friends in dictionary
        return max(most_followed_friend, key = most_followed_friend.get)

    def to_dot(self):
        result = []
        result.append('digraph {')
        result.append('    layout=neato')
        result.append('    overlap=scalexy')
        for user in self.list_users():
            for friend in self.get_friends(user):
                result.append('    "{}" -> "{}"'.format(user, friend))
        result.append('}')
        return '\n'.join(result)


def create_network_from_file(filename):
    '''Create a SocialNetwork from a saved file

    Arguments:
        filename (str): The name of the network file

    Returns:
        SocialNetwork: The SocialNetwork described by the file
    '''
    network = SocialNetwork()
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            users = line.split()
            network.add_user(users[0])
            for friend in users[1:]:
                network.add_friend(users[0], friend)
    return network


def main():
    network = create_network_from_file('simple.network.txt')
    print(network.to_dot())
    print(network.suggest_friend('francis'))


if __name__ == '__main__':
    main()
