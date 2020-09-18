print('Welcome to my first game')

name = input('Whath is your name? ')
age = int(input('What  is your age? '))
health = 10


if age >= 18:
    print('you are old enought')

    wants_to_play=input('Do you want to play?  ').lower()
    
    if wants_to_play == 'yes':
        print('Lets play!')
        print('You starting the game with', health,'health')

        left_or_right = input('Ook first choise... Do you want to go left or right (left/right)? ')

        if left_or_right == 'left':
            ans = input('Nice , you follow the path and reach a lake ... Do you swim across or go around (across/around) ?')

            if ans == 'around':
                print('You went around the lake and reached the other side of the lake')
            elif ans == 'across':
                print('You managed to get across the lake ,  but were bit by a fish and lost 5 health ')
                health -= 5
            else:
                print('You lost')        
        else:
            print('You fell down and lost') 
    else:
        print('See you later !')
else:
    print('You are not old enough to play')
















'''
 Data type:
str     'hello', "World" , "89"
int       5, -90 , 1000 , -43
float        5.3 ,3.5, 6.7 ,-100.0
bool      true || false
'''