def subdomainVisits(cpdomains):
    from collections import Counter
    res=Counter()
    for words in cpdomains:
        cou,word=words.split(" ")
        cou=int(cou)
        frag=word.split(".")
        for i in range(len(frag)):
            res[".".join(frag[i:])]+=cou

    return ["{}{}".format(ct,dom) for dom,ct in res.items()]

