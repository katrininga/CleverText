#CleverText is a text knob connected to a switch node
#Switch node is connected to Read nodes, whatever the switch node is set on and is connected, cleverText will add its filename into text knob

clever_text = nuke.toNode(“CleverText”)
node = clever_text.input(0)

node.knob(“knobChanged”).setValue(‘’’
read_node = node.input(int(swhich)))
clever_text[“message”].setValue(“[basename [value “ + read_node +[“name”].getValue() + “.file]]”)
“””)
