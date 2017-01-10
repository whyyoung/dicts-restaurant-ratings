# your code goes here

def build_restaurant_ratings(filename):
    rating_file = open(filename)
    restaurant_ratings = {}

    for line in rating_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')

        restaurant_ratings[restaurant] = rating

    return restaurant_ratings

def print_restaurant_rating(dictionary):

    for restaurant, rating in sorted(dictionary.iteritems()):
        dictionary[restaurant] = dictionary.get(rating)
        print "{} is rated at {}.".format(restaurant, rating)

our_yelp = build_restaurant_ratings("scores.txt")
user_restaurant = raw_input("What restaurant would you like to rate: ")
user_rating = int(raw_input("What would you like to rate the restaurant: "))

our_yelp[user_restaurant] = user_rating

print_restaurant_rating(our_yelp)
