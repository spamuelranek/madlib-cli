import re

with open("assets/dark_and_stormy_night_template.txt","w") as dark_stormy:
  dark_stormy.write("It was a {Adjective} and {Adjective} {Noun}.")

def read_template(file_path):
  with open(file_path,"r") as line_template:
    return line_template

dark_stormy_template = read_template("assets/dark_and_stormy_night_template.txt")
  
def parse_template(line_template):
  pattern = r"\{(\w+)\}"
  actual_stripped = re.sub(pattern,"{}", line_template)
  actual_parts = tuple(re.findall(pattern,line_template))
  return (actual_stripped,actual_parts)
  
  
def merge(stripped_line,user_words):
  detouple_user_words = ",".join(user_words)
  new_string = stripped_line.format(detouple_user_words)
  return new_string