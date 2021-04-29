import os

ignore = [
    './.git',
    './Compete-McGill-2020',
    './Practice',
    './USACO',
    './Rosetta',
    './Scripts',
    './Lib',
    './Contest',
]

def main():
    d = {}
    for root, dirs, files in os.walk(".", topdown=True):
        if sum([x in root for x in ignore]) or root == '.':
            continue
        d[root[2:]] = len(os.listdir(root))

    ret = "## solutions\n\nCompetitive programming & interview style problems I have solved on various coding platforms.\n\n### Contents\n"
    for k, v in sorted(d.items()):
        l = "%20".join(k.split())
        ret += "[{}](https://github.com/terror/CompetitiveProgramming/blob/master/{}/) ({})<br/>\n".format(k, l, v)
    print(ret)


if __name__ == '__main__':
    main()
