my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def make_tuple(the_dict):
  the_tuple = list(tuple(the_dict.items()))
  print(the_tuple)

make_tuple(my_dict)
