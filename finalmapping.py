import json,pprint


def flatten_dict(d, key="",mapp={}):
    for k, v in d.iteritems():

        value = v
        if type(value) == dict:
            #key = key + "_" + k
            flatten_dict(value,key + "_" + k)
        if type(value) == list:
            flatten_lis(value, key + "_" + k)
        else:
            mapp.update({key + "_" + k: value})
    return mapp


def flatten_lis(v, k):
    lis = []
    for each in v:
        if type(each) == dict:
            lis.append(flatten_dict(each, k))
        if type(each) == list:
            lis.append(flatten_lis(each, k))
        else:
            lis.append({k:v})
            break
    return lis

f = open("testinput.json", "r+")
data = json.loads(f.read())
final=[]
for k, v in data.iteritems():
    if type(v) == dict:
        data1 = flatten_dict(v,k)
        final.append(data1)

    elif type(v) == list:
       data2= flatten_lis(v,k)
       final.append(data2)
    else:
        data = {k:v}
        final.append(data)

new=[]
for entries in final:
    if type(entries)== list:
        for each in entries:
            #print each
            new.append(each)
    else:
        new.append(entries)

d={}
for dis in new:
    for k, v in dis.iteritems():
        if type(v) != dict:
            d.update({k:v})
pprint.pprint(d)


