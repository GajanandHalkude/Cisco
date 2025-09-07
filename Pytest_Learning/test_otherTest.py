def test_wallet():
    print("Wallet tested")
def test_money():
    print("You have info money")
def test_buyItems():
    print("Bought items")
def test_order():
    print("Order delivered")

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

def test_numbers_fail():
    number_to_text1 = {str(x): x for x in range(5)}
    number_to_text2 = {str(x * 10): x * 10 for x in range(5)}
    for i,j in number_to_text1:
        print(i , j)
    print(number_to_text1)
    assert number_to_text1 == number_to_text2 
    
def test_long_text_fail():
    long_text = "Lorem ipsum dolor sit amet " * 10
    assert "hello world" in long_text