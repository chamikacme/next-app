import textwrap


text1="Don't surround yourself with food or ready to eat snacks"
subtext1 = "The more food in front of you, the more you'll eat or want to eat. This is basic human psychology. To stop yourself from munching endlessly, keep food, especially the fattening, tempting ones, a little out of range."

def wrapAction(text1, subtext1):
    wrapper = textwrap.TextWrapper(width=30)
    headList = wrapper.wrap(text=text1)

    wrapper2 = textwrap.TextWrapper(width=50)
    bodyList = wrapper2.wrap(text=subtext1)

    return headList, bodyList

headList, bodyList = wrapAction(text1, subtext1)

for element in headList:
	print(element)
	print("----------------------------------------")

for element in bodyList:
	print(element)
	print("----------------------------------------")
