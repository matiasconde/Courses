## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)

def line1(line):
    line[0] = line[0].replace("hamlet@","")
    return line

hamlet_with_ids = split_hamlet.map(lambda line: line1(line))
hamlet_with_ids.take(25)    


## 3. Remove Blank Values ##

hamlet_with_ids.take(5)

hamlet_text_only0 = hamlet_with_ids.filter(lambda line: len(line)>1)

hamlet_text_only = hamlet_text_only0.map(lambda line: [l for l in line if l!=""])
hamlet_text_only.take(15)

## 4. Remove Pipe Characters ##

hamlet_text_only.take(10)

def final_clean(line): 
    new_line = list()
    for element in line: 
        if element == "|":
            pass
        elif "|" in element:
            new_line.append(element.replace("|",""))
        else: new_line.append(element)
    return new_line

clean_hamlet = hamlet_text_only.map(lambda x: final_clean(x))
#clean_hamlet.take(10)

