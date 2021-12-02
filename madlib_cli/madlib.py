import re

with open("assets/dark_and_stormy_night_template.txt","w") as dark_stormy:
  dark_stormy.write("It was a {Adjective} and {Adjective} {Noun}.")

with open("assets/a_wild_ride_to_the_back.txt","w") as wild_ride:
  wild_ride.write("""
  While I {past tense verb} to the {noun} something happened.
  There is a {singular noun} in the {noun}. It {past tense verb} a {noun}.
  That {same noun as previous} {verb ending in ed} though the {noun}.
  There was no {verb ending in ing} it.
  """)

def welcome_message():
  print("""
    Welcome to SUPER Whacky MADlibs
    To play please type: START
    You will recieve a list of types of words.
    Please input a corresponding type of word into the input
    e.g. Noun 
    input fish
    To stop input: quit
    """)

def madlib():
  welcome_message()
  player_input = input("> ")
  if player_input == "START":
    player_typed_quit = False
  while not player_typed_quit:
    if player_input == "quit":
      player_typed_quit = True
    else:
      line_template = read_template("assets/a_wild_ride_to_the_back.txt")
      deconstructed_line_template = parse_template(line_template)
      list_of_words_to_fulfill = list(deconstructed_line_template[1])
      player_response_as_tuple =ask_for_words(list_of_words_to_fulfill, player_typed_quit)
      finalized_madlib = merge(deconstructed_line_template[0],player_response_as_tuple)
      need_to_write_this_one_down(finalized_madlib)
      print(finalized_madlib)
      player_typed_quit = True
  print("Thanks for Playing")

def need_to_write_this_one_down(finished_madlib):
  split_madlib = finished_madlib.split("\n")
  polished_title_madlib = split_madlib[1][2:].replace(" ","_")
  with open(f"assets/{polished_title_madlib}.txt","w") as new_file:
    new_file.write(finished_madlib)

def ask_for_words(list_of_types_of_words, player_typed_quit):
  player_input_words = []
  for word in list_of_types_of_words:
    response_from_input = input(f"{word} : ")
    if response_from_input == 'quit':
      player_typed_quit = True
      return player_typed_quit
    player_input_words.append(response_from_input)
  return tuple(player_input_words)


def read_template(file_path):
  with open(file_path,"r") as line_template:
    return line_template.read()

dark_stormy_template = read_template("assets/dark_and_stormy_night_template.txt")
  
def parse_template(line_template):
  pattern = r"\{(\w+\s*\w+\s*\w+\s*\w+)\}"
  actual_stripped = re.sub(pattern,"{}", line_template)
  actual_parts = tuple(re.findall(pattern,line_template))
  return (actual_stripped,actual_parts)
  
  
def merge(stripped_line,user_words):
  new_string = stripped_line.format(*user_words)
  return new_string

madlib()