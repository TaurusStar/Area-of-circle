from math import pi

def area_of_circle(r):
    a = pi*r*r
    return a

def main():
    while True:
        r = input('Give the radius of a circle that you need its area:')
        area = area_of_circle(r)
        print('The area of this circle is:',area)
        s = input("Type 'stop' to stop this program Or it will continue:")
        if s == 'stop':
            break
main()



    

    


