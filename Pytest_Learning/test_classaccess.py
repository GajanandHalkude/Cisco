class ExternalClass:
    def external_method(self):
        return "Hello"
class InternalClass:
    def test_assertion(self):
        ex_instance = ExternalClass()
        assert ex_instance.external_method == "Hello"

#####
import pytest
import pdb
@pytest.fixture
def order():
    return []

@pytest.fixture
def c1(order):
    return order.append("c1")

@pytest.fixture
def c2(order):
    return order.append("c2")

class TestClassWithAutoUse:
    @pytest.fixture(autouse= True)
    def c3(self,order,c2):
        pdb.set_trace()
        order.append("c3")
    
    def test_req(self,order,c1):
        pdb.set_trace()
        order.append("c4")
        assert order == ["c2","c3","c1","c4"]

    def test_not_req(self,order):
        pdb.set_trace()
        order.append("c4")
        assert order == ["c2","c3","c4"]

class TestClassWithoutAutouse:
    def test_req(self,order,c1):
        assert order == ["c1"]
        
    def test_no_req(self,order):
        assert order == []

    
