"""Write a function:

analyze(*strings, reverse=False)

Requirements:

Accept any number of strings using *args.
If reverse=False, print each string normally.
If reverse=True, print each string reversed."""

def analyze(*string, reverse=False):
    m=""
    n=""
    if reverse==False:
        m=string
        print(m)
    else:
        for i in range(len(string)-1,-1,-1):
            m += string[i]
            for t in range(len(string[i])-1,-1,-1):
                n += string[i][t]
        print(n)

analyze("himyname","waow yohohohoho","kaakidikadaaoo", reverse = True)