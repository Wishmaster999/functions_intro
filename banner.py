def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text("  ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

result = banner_text("Nothing is returned")
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())


def banner_text(text: str = "", screen_width: int = 88) -> None:
    """ Print a string centred, with ** either side.

   :param text: The string to print.
       An asterisk (*) will result in a row of asterisks.
       The default will print a blank line, with a ** border at
       the left and right edges.
   :param screen_width: The overall width to print within
       (including the 4 spaces for the ** either side).
   :raises ValueError: if the supplied string is too long to fit.
   """
    if len(text) > screen_width - 4:
        raise ValueError("String '{0}' is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 70)
banner_text("Don't be silly chumps,", 70)
banner_text("Just purse your lips and whistle - that's the thing!", 70)
banner_text("And... always look on the bright side of life...", 70)
banner_text("*", 70)

