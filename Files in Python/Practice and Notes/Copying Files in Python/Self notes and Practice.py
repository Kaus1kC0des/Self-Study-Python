friends = input("Enter your friends name: ").title().split()
people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)
friends_nearby = set(friends_set.intersection(people_nearby_set))
print(friends_nearby)
nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby:
    print(f"Your friend {friend} is nearby. Meet up with them.")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()