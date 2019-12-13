hex_colours_dict={"aliceblue:":"#f0f8ff","antiquewhite":"#faebd7",
                  "aquarmarine1":"#7fffd4","azure1":"#f0fff",
                  "brown":"#a52a2a","blueViolet":"#8a2be2",
                  "blanchealmond":"#ffebcd","black":"#00000",
                    "chocolate":"#d2691e","cyan1":"#00ffff"}


while True:
    color_input = input("Please input the color:")
    color_input=color_input.lower()
    if not color_input:
        print("see you")
        break
    if(color_input in hex_colours_dict):
        print("{} is {}".format(color_input,hex_colours_dict[color_input]))
    else:
        print("{} is not in hex colour dictionary".format(color_input))


