#!/usr/bin/python
def empresa(num):
    if(num < 30000000 or num >= 60000000):
        return "fuera"

    if (((30000000<= num) and (num <= 33599999)) or ((40000000<= num) and (num <= 40999999)) or ((44760000<= num) and (num <= 46999999)) or ((47730000<= num) and (num <= 48199999)) or ((48220000<= num) and (num <= 50099999)) or ((50300000<= num) and (num <= 50699999)) or ((51500000<= num) and (num <= 52099999)) or ((53000000<= num) and (num <= 53099999)) or ((53140000<= num) and (num <= 53899999)) or ((55200000<= num) and (num <= 55299999)) or ((55500000<= num) and (num <= 55539999)) or ((55800000<= num) and (num <= 55819999)) or ((57000000<= num) and (num <= 57099999)) or ((57190000<= num) and (num <= 57899999)) or ((58000000<= num) and (num <= 58099999)) or ((58190000<= num) and (num <= 58199999)) or ((58800000<= num) and (num <= 59099999)) or ((59180000<= num) and (num <= 59199999)) or ((59900000<= num) and (num <= 59999999))):
        return "tigo"

    elif (((34000000<= num) and (num <=34699999)) or ((43000000<= num) and (num <=44759999)) or ((50200000<= num) and (num <=50299999)) or ((50700000<= num) and (num <=51099999)) or ((51400000<= num) and (num <=51499999)) or ((52100000<= num) and (num <=52999999)) or ((53120000<= num) and (num <=53139999)) or ((53900000<= num) and (num <=54099999)) or ((55000000<= num) and (num <=55099999)) or ((55180000<= num) and (num <=55199999)) or ((55400000<= num) and (num <=55429999)) or ((55450000<= num) and (num <=55499999)) or ((56000000<= num) and (num <=56099999)) or ((56400000<= num) and (num <=56899999)) or ((57900000<= num) and (num <=57999999)) or ((59150000<= num) and (num <=59179999)) ):
        return "movistar"

    elif(((41000000<= num) and (num <=42999999)) or ((47000000<= num) and (num <=47729999)) or ((50100000<= num) and (num <=50199999)) or ((51100000<= num) and (num <=51399999)) or ((53100000<= num) and (num <=53119999)) or ((54100000<= num) and (num <=54999999)) or ((55100000<= num) and (num <=55179999)) or ((55300000<= num) and (num <=55399999)) or ((55430000<= num) and (num <=55449999)) or ((55540000<= num) and (num <=55799999)) or ((55820000<= num) and (num <=55999999)) or ((56100000<= num) and (num <=56399999)) or ((56900000<= num) and (num <=56999999)) or ((57100000<= num) and (num <=57189999)) or ((58100000<= num) and (num <=58189999)) or ((58200000<= num) and (num <=58799999)) or ((59100000<= num) and (num <=59149999)) or ((59200000<= num) and (num <=59899999))):
        return "claro"

    else:
        return "otro"

    return "bla"

este = empresa(54645757)
print(este)