class Color:
    
    background_colors = {"red":[255, 0, 0], "green":[0, 255, 0], "blue":[0, 0, 255]}

    def background(red, green, blue):
        return "\033[48;2;" + str(red) + ";" + str(green) + ";" + str(blue) + "m"
    
    def foreground(red, green, blue):
        return "\033[38;2;" + str(red) + ";" + str(green) + ";" + str(blue) + "m"
    
    def reset():
        print("\033[0m")
