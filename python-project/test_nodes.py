from nodes import set_current_node

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def test_set_current_node():
    try:
        inf = 999999
        count = set_current_node({"A"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5})
        assert count == "F", 'set_current_node({"A"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5}), expected "F", got {}.'.format(count)
        count = set_current_node({"A","F"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5})
        assert count == "F", 'set_current_node({"A","F"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5}), expected "E", got {}.'.format(count)
        success()

        seng_msg("Good job!","Correct. You need to pick the non-visited node with the smallest distance.")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Check the solved example again.")

if __name__ == "__main__":
    test_set_current_node()
