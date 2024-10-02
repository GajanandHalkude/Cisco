#VarArgs takes any no of inputs from user, *args
class VarArgs:

    #Non keyworded argumnet list
    def variable_length_arguments(*args):
        for arg in args:
            print(f"{arg}")
    variable_length_arguments(1,2,3,4,"input","output")

    #keyworded argumnet list. accepts key and value type args
    def dict_type_args(**args):
        for key,value in args.items():
            print(f"{key} : {value}")
    dict_type_args(fname="Gajanand",lname="Halkude",city="Hyderabad")

class CombinedVarArgs:
    def varagrs(*vargs,**kwargs):
        for arg in vargs:
            print(f"{arg}")
        for key , val in kwargs.items():
            print(f"{key} : {val}") 

comb = CombinedVarArgs.varagrs(10,20,30,
                               state = "Telangana",dist = "Kamareddy",mandal="Jukkal")
