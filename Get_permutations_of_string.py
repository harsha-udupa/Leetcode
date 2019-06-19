


# Input string with size 0-10000. Charectors can be repetitiveself.



def get_permuation(counts,l,r,result):
    if l==r:
        result.append(counts)

    for i,j in enumerate(counts):
        counts[i],counts[l]=counts[l],counts[i]
        get_permuation(counts,l+1,r,result)
        counts[i],counts[l]=counts[l],counts[i]

def main():
    string=raw_input("Enter the input string\n")
    result=[]
    get_permuation(string,0,len(string)-1,result)

    print result


if __name__=="__main__":
    main()
