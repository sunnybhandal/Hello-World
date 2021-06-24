
# THE STORY APP
first_story = [
  # Title
  "Billy",
  "Hey NAME, I missed you! The guy was VERB.",
  # Replacements
 [
   ["Give a name: ", "NAME"],
   ["Give a verb: ", "VERB"]
 ]
]

second_story = [
  # Title 
  "Waterfall",
  "The water fell SPEED, as I ate my FOOD",
  # Replacements
  [
    ["What is the speed of the fall? ", "SPEED"],
    ["What are you eating? ", "FOOD"]
  ]
]

stories = [
 first_story,
 second_story
]

pick = int(input("What story would you like? "))
story = stories[pick]
story_str = story[1]
replacements = story[2]

for prompt, replacement in replacements:
  userInput = input(prompt)
  final_story = story_str.replace(replacement, userInput)

print(final_story)

#  PRINT THE TITLES
for index, story in enumerate(stories):
  title = story[0]
  print(str(index) + "-" + title)
  