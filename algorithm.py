import dash
import dash_core_components as dcc
import dash_html_components as html

print("In this program, the age-standardized mortality rate from COVID-19 for a sub population can be found by comparing the sub-population to a standard population. ")
print("This program uses deep learning to help solve the problem: ")
print("Which states in the United States of America have had the highest death rates due to COVID-19 when removing age as a confounding variable?\n")
a = input("What is the name of the town/city/state/country/continent that will act as the sub-population?\n")
b = input("\nWhat is the name of the town/city/state/country/continent that will act as the standard population?\n")

def algorithm():
    c = input("\nWhat is one age range of " + a + "?\n")
    d = int(input("\nWhat is the total population in " + a + " within the ages of " + c + "?\n"))
    e = int(input("\nHow many deaths did " + a + " suffer within the age range of " + c + " due to COVID-19?\n"))
    f = e/d*100000
    print("\nThe crude mortality rate due to COVID-19 for the age range of " + c + " per 100,000 people in " + a + " is: ")
    print(f)
    g = int(input("\nWhat is the population of " + b + " within the age range of " + c + "?\n"))
    h = f*g/100000
    i = int(input("\nHow many deaths did " + b + " suffer within the age range of " + c + " due to COVID-19?\n"))
    j = i/g*100000
    print("\nThe crude mortality rate for the age range of " + c + " per 100,000 people in " + b + " is: ")
    print(j)
    print("\nThe expected number of deaths in " + b + " within the age range of " + c + " is: ")
    print(h)
    
    B = int(input("\nHow many deaths did " + b + " suffer in ALL?\n"))
    _ = int(input("\nWhat is the total population of " + b + " ?\n" ))
    print("\nThe overall crude mortality per 100,000 people due to COVID-19 in " + b + " is:\n")
    _B = (B/_)*100000
    print(_B)
    k = input("\nWould you like to include more age ranges to make the final age-standardized rate more accurate? (Y or N) \n")

    def app():        
        app = dash.Dash()

        app.layout = html.Div(children=[
            html.H1('Graph'),
            dcc.Graph(id='example',
                    figure ={
                        'data': [
                            {'x':[a, b], 'y':[A, _B], 'type':'bar', 'name':'ASMR'},
                            ],
                        'layout': {
                            'title': 'Comparison of Age-Standardized Mortality Rate and Crude Mortality Rate due to COVID-19 '
                            }
                        })
            ])

        if __name__ == '__main__':
            app.run_server(debug=True)

    if k == "Y":
        z = h
        y = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h/g)
        print(A)
        app()
        quit()
    algorithm()
    if k == "Y":
        x = h
        w = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z)/(g+y)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        v = h
        u = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x)/(g+y+w)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        t = h
        s = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v)/(g+y+w+u)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        r = h
        q = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t)/(g+y+w+u+s)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        p = h
        o = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r)/(g+y+w+u+s+q)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        n = h
        m = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p)/(g+y+w+u+s+q+o)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        Z = h
        Y = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n)/(g+y+w+u+s+q+o+m)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        X = h
        W = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z)/(g+y+w+u+s+q+o+m+Y)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        V = h
        U = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X)/(g+y+w+u+s+q+o+m+Y+W)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        T = h
        S = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V)/(g+y+w+u+s+q+o+m+Y+W+U)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        R = h
        Q = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T)/(g+y+w+u+s+q+o+m+Y+W+U+S)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        P = h
        O = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        N = h
        M = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        L = h
        K = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        J = h
        I = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N+L)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M+K)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        H = h
        G = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N+L+J)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M+K+I)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        F = h
        E = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N+L+J+H)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M+K+I+G)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        D = h
        C = g
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N+L+J+H+F)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M+K+I+G+E)
        print(A)
        quit()
    algorithm()
    if k == "Y":
        print("More age ranges cannot be added. The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        A = (h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N+L+J+H+F+D)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M+K+I+G+E+C)
        print(A)
        quit()
    else: 
        print("The age-standardized mortality rate of " + a + ", after being compared to " + b + ", is: ")
        print((h+z+x+v+t+r+p+n+Z+X+V+T+R+P+N+L+J+H+F+D)/(g+y+w+u+s+q+o+m+Y+W+U+S+Q+O+M+K+I+G+E+C))
        quit()

algorithm()
