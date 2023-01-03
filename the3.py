
def calculate_price(part_list):
    tree = maketree(part_list)
    rprice = price_helper(tree, 1, 0)
    return rprice

def price_helper(stree, n, price):
    n = n * stree[0]
    for i in stree:
        if type(i)==list:
            price = price_helper(i,n,price)
        if type(i)==float:
            price += n * i
    return price

def maketree(part_list):
    for i in range(len(part_list)):
        for j in range(len(part_list[i])):
            if type(part_list[i][j]) == tuple:
                part_list[i][j] = list(part_list[i][j])
    leaf1 = []
    others1 = []
    for i in range(len(part_list)):
        if type(part_list[i][1]) == float:
            leaf1.append(part_list[i])
        else:
            others1.append(part_list[i])
    tree = helper(leaf1, others1)
    return tree

def helper(leafs, others):
    first_leafs = leafs[:]
    result_others = []
    result_leafs = leafs[:]
    for i in range(len(others)):
        elemaninaradegeri = others[i][:]
        araleaf = []
        status = "changed"
        for j in range(len(others[i])):
            if j == 0: continue
            if len(elemaninaradegeri[j]) == 3: continue
            if status == "iptal":
                break
            for k in range(len(first_leafs)):
                if others[i][j][1] == first_leafs[k][0]:
                    if first_leafs[k] != elemaninaradegeri[j][1:]:
                        elemaninaradegeri[j].extend(first_leafs[k][1:])
                        araleaf.append(first_leafs[k])
                    if j == len(others[i]) - 1:
                        result_leafs.append(elemaninaradegeri)
                        for m in range(len(araleaf)):
                            result_leafs.remove(araleaf[m])
                    break
                if k == len(first_leafs) - 1 and others[i][j] == elemaninaradegeri[j]:
                    status = "iptal"
                    result_others.append(elemaninaradegeri)
                    break
    if result_others != []:
        return helper(result_leafs, result_others)
    if result_others == []:
        last_result_leafs = result_leafs[-1]
        last_result_leafs.insert(0,1)
        return last_result_leafs

def required_parts(part_list):
    tree = maketree(part_list)
    result = []
    result = required_helper(tree, 1, result)
    return result

def required_helper(stree2, n, result):
    n = n * stree2[0]
    for i in range(len(stree2)):
        if i > 1:
            if type(stree2[i])==list:
                required_helper(stree2[i],n,result)
            if type(stree2[i])==float:
                if (n, stree2[i - 1]) in result: continue
                result.append((n,stree2[i-1]))
    return result

def stock_check(part_list, stock_list):
    requiredlst = required_parts(part_list)
    result = []
    checked = []
    for i in range(len(requiredlst)):
        for j in range(len(stock_list)):
            if requiredlst[i][1] in stock_list[j]:
                checked.append(requiredlst[i])
                if requiredlst[i][0] > stock_list[j][0]:
                    result.append((requiredlst[i][1],requiredlst[i][0]-stock_list[j][0]))

    for i in range(len(requiredlst)):
        if not requiredlst[i] in checked:
            result.append(requiredlst[i][::-1])
    return result


