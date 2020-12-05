print("Select any bolow word if you want to find meaning. (also word is case sensitive):")
inp=input("Computer,CPU,MotherBoard,programming\n")
dict1 = {"Computer": "A computer is a machine that can be instructed to carry out "
                     "sequences of arithmetic or "
                     "logical operations automatically via computer programming."
        , "CPU": "A central processing unit (CPU), "
                 "also called a central processor, "
                 "main processor or just processor"
         ,"MotherBoard": "T he motherboard is a printed circuit board and "
                   "foundation of a computer that is the "
                   "biggest board in a computer chassis. I"
                   "t allocates power and allows communication "
                   "to and between the CPU, RA"
                   "M, and all other computer hardware components."
         ,"programming":"the process of writing computer programs"}
print(dict1[inp])
