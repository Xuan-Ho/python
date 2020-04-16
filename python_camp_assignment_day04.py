"""
Significant parts of the code to make the program demonstrated on the previous page have been deleted.
(Please use whatever bands or musical acts you enjoy instead of Mark’s!)Correctly write the missing code so
that you have a working program in your console.Note that \n is a character entity the moves to the next line
within a string. Also note that the line bandRatings = {} creates an empty dictionary.Post a screenshot of you
with your working output (not the code) to the console.
"""

bands = (
    "Journey",
    "REO Speedwagon",
    "Styx",
    "Mr. Mister",
    "The Cure",
    "The Doobie Brothers",
    "Neil Diamond",
    "The Beatles",
    "Live",
    "TinaTurner" ,
    "The Guess Who"
)

bandRatings = {}

# Populates bandRatings dictionary with band and user's input scores
for band in bands:
    print("Rate " + band + ". (1-10)")
    u_input = input("")
    bandRatings.update({band: u_input})
    #print(band, ":", u_input)
    print(bandRatings.keys(), "\n")  # Print the current set items

totalRatings = 0  # Total Ratings Scores
numRatings = 0  # Total Bands Rated

# Set up Ratings metadata
print("\nYour Ratings:")
for k, v in bandRatings.items():
    print(k + ":" + v)
    totalRatings = totalRatings + int(v)
    numRatings = numRatings + 1

average = totalRatings/numRatings  # store user's average rating score

print("\nTotal Rantings: " + str(totalRatings))
print("Number of Ratings: " + str(numRatings))
print("\nYour average rating is a: " + str(average))

# Print all bands
for x in bandRatings.keys():
    print(x)
print("\n\n")

# print all rating scores
for y in bandRatings:
    print(bandRatings[y])
    


