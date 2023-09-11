from utils import utils

class utils_tests:
    
    # test reversed function
    def reverse_test(self):
        
        utils_obj = utils()
        
        #positive int
        assert(utils_obj.reversed(123) == 321)
        assert(utils_obj.reversed(5428754) == 4578245)
        #negative int
        assert(utils_obj.reversed(-5678) == -8765)
        #float
        assert(utils_obj.reversed(10.0) == None)
        #string
        assert(utils_obj.reversed("1468") == None)
      
    # test formatter function
    def formatter_test(self):
    
        utils_obj = utils()
    
        #positive int
        assert(utils_obj.formatter(123) == ('0b1111011', '0o173'))
        assert(utils_obj.formatter(5428754) == ('0b10100101101011000010010', '0o24553022'))
        #negative int
        assert(utils_obj.formatter(-5678) == ('-0b1011000101110', '-0o13056'))
        #float
        assert(utils_obj.formatter(10.0) == (None, None))
        #string
        assert(utils_obj.formatter("1468") == (None, None))
        
    def run_tests(self):
    
        self.reverse_test()
        self.formatter_test()
        
        
        
utils_tests_obj = utils_tests()

utils_tests_obj.run_tests()
    
    