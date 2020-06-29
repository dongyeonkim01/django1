import re
class regexClass():

    def __init__(self,data):
        self.data = data

    def openFile(self):
        with open(self.data, 'r') as f:
            text = f.readlines()
            text = ''.join(text)
        return text


    def container_reg(self,text):
        patten      = re.compile('\S+', re.M)
        key,val     ='',''
        bools  ,st  = False,False
        counts      = 0
        tmp_kes     = ''

        for i in text.split('\n'):
            if 'container' in i:
                bools = True
            if bools:
                li = patten.findall(i)
                val = val + ' \n ' + i
                for inner in li:
                    if st:
                        if inner == '{':
                            counts +=1
                        elif inner == '}':
                            counts -=0
                        if counts ==0:
                            bools = False
                    else:
                        if inner =='{':
                            key = tmp_kes
                            counts +=1
                            st = True
                        elif inner =='}':
                            return False
                    tmp_kes = inner
        return key, val

    def container_dicOut(self):
        dic = {}
        tt = ''
        cc = 0
        bb = False
        data = self.openFile()
        for i in data.split('\n'):
            if 'container' in i :
                bb = True

            if bb:
                tt = tt + '\n' + i
                if '{' in i:
                    cc += 1
                if '}' in i:
                    cc -= 1
                if cc ==0:
                    bb = False
                    k,v = self.container_reg(tt)
                    dic[k] = v
                    tt = ''

        for kkk in dic.keys():
            print('key : ',kkk,' /// val::',dic[kkk])
        return dic


    def leaf_reg(self,text):
        patten      = re.compile('\S+', re.M)
        key,val     = '',''
        bools  ,st  = False,False
        counts      = 0
        tmp_kes     = ''

        for i in text.split('\n'):
            if 'leaf' in i:
                bools = True
            if bools:
                li = patten.findall(i)
                val = val + ' \n ' + i
                for inner in li:
                    if st:
                        if inner == '{':
                            counts +=1
                        elif inner == '}':
                            counts -=0
                        if counts ==0:
                            bools = False
                    else:
                        if inner =='{':
                            key = tmp_kes
                            counts +=1
                            st = True
                        elif inner =='}':
                            return False
                    tmp_kes = inner
        return key, val

    def leaf_dicOut(self):
        dic = {}
        tt = ''
        cc = 0
        bb = False
        data = self.openFile()
        for i in data.split('\n'):
            if 'leaf' in i :
                bb = True

            if bb:
                tt = tt + '\n' + i
                if '{' in i:
                    cc += 1
                if '}' in i:
                    cc -= 1
                if cc ==0:
                    bb = False
                    k,v = self.leaf_reg(tt)
                    dic[k] = v
                    tt = ''

        # for kkk in dic.keys():
        #     print('key : ',kkk,' /// val::',dic[kkk])
        return dic


    def final_config(self,dic):
        html_text,out_html = '',''
        with open(self.data, 'r') as f1:
            text = f1.readlines()
        html_text = '\n'.join(text)
        patten = re.compile('\S+', re.M)
        for i in text:

            if '<em>' in i:
                lli = patten.findall(i)
                bool =False
                ins = 0
                for ind,val in enumerate(lli):
                    if val=='<em>':
                        ins = ind
                lli[ins] = '<em  onclick=" ' + " jq(' " + str(dic[lli[ins+1]]).replace("\n",'').replace('"','') + " ' )" + ' " >'
                i = ''.join(lli)
            out_html += i
        return out_html




if __name__ == "__main__":
    A = regexClass('test.yang')
    tex = str(A.leaf_dicOut())
    dic = A.leaf_dicOut()
    # print(type(dic))
    Test = regexClass('out.html')
    print(Test.final_config(dic))


    # with open('test.txt','w') as f1:
    #     f1.write(tex)
