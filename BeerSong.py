### 337 programming project! 
# song project #

Ninety_Nine_Bottles_of_Beer = 100
while Ninety_Nine_Bottles_of_Beer > 0:
    Ninety_Nine_Bottles_of_Beer = Ninety_Nine_Bottles_of_Beer - 1
    print(Ninety_Nine_Bottles_of_Beer, "bottles of beer on the wall,"
          ,Ninety_Nine_Bottles_of_Beer, "bottles of beer",
          "\ntakeone down, pass it around"
          , (Ninety_Nine_Bottles_of_Beer - 1),
          "Bottles of beer on the wall")
    if Ninety_Nine_Bottles_of_Beer <= 3:
        print(" 2 bottles of beer on the wall, 2 bottles of beer")
        break



