from flask import Flask, render_template, request, json
import re
app = Flask(__name__)

def isNumber(user_input):
	it_is = False
	try:
		float(user_input)
		it_is = True
	except ValueError:
		it_is = False
	return it_is

def swap(arr):
	aux = 0
	n =len(arr)
	i = 0
	j = n-1

	while i < n:
		if i < j:
			aux = arr[i]
			arr[i] = arr[j]
			arr[j] = aux
		j = j - 1
		i = i + 1

	return arr

def suma(arr1,arr2,c1,c2,n):
	arrRes=[]
	i=0
	r=c1-c2
	arrLen1 = arrLen1
	arrLen2 = arrLen2
	while i<n:
		if i < r:
			arrRes.append(float(arr1[i]))
		else:
			if i < arrLen1 or i < arrLen2:
				arrRes.append(float(arr1[i])+float(arr2[i-r]))
			else:
				if i >= arrLen2:
					arrRes.append(float(arr1[i]))
				else:
					arrRes.append(float(arr2[i-r]))
		i=i+1
	return arrRes

def resta(arr1,arr2,c1,c2,n):
	arrRes=[]
	i=0
	r=c1-c2
	rAbs=0
	if r<0:
		rAbs=abs(r)
	arrLen1 = len(arr1)
	arrLen2 = len(arr2)
	val = True

	while i<n:
		if i < r:
			arrRes.append(float(arr1[i]))
		else:
			if r < 0 and val:
				if i < rAbs:
					arrRes.append(float(arr2[i]*(-1)))
				else:
					val = False
			else:
				if i < arrLen1 or i < arrLen2:
					arrRes(float(arr1[i])-float(arr2[i-r]))
				else:
					if i >= arrLen2:
						arrRes.append(float(arr1[i]))
					else:
						arrRes.append(float(arr2[i-r]))
		i=i+1
	return arrRes

def multi(arr1,arr2,c1,c2,n):
	arrRes=[]
	i=0
	r=c1-c2
	arrLen1 = len(arr1)
	arrLen2 = len(arr2)

	while i<n:
		if i < r:
			arrRes.append(float(arr1[i]))
		else:
			if i < arrLen1 or i < arrLen2:
				arrRes.append(float(arr1[i])*float(arr2[i-r]))
			else:
				if i >= arrLen2:
					arrRes.append(float(arr1[i]))
				else:
					arrRes.append(float(arr2[i-r]))
		i=i+1
	return arrRes

def division(arr1,arr2,c1,c2,n):
	arrRes=[]
	i=0
	r=c1-c2
	rAbs=0
	if r<0:
		rAbs=abs(r)
	arrLen1 = len(arr1)
	arrLen2 = len(arr2)
	val = True

	while i<n:
		if i < r:
			arrRes.append(float(arr1[i]))
		else:
			if r < 0 and val:
				if i < rAbs:
					arrRes.append(0)
				else:
					val = False
			else:
				if i < arrLen1 or i < arrLen2:
					arrRes(float(arr1[i])/float(arr2[i-r]))
				else:
					if i >= arrLen2:
						arrRes.append(float(arr1[i]))
					else:
						arrRes.append(float(arr2[i-r]))
		i=i+1
	return arrRes

def desplazamiento(arr,d):
	i = 0
	if d > 0:
		while i < d:
			arr.append(0)
			i = i + 1
	else:
		while i > d:
			arr.insert(0,0)
			i = i - 1
	return arr

def diezmar(arr,c,d):
	i = 0
	n = len(arr)
	arrRes = []
	aux = 0
	while i < n:
		aux = d*i
		if i < c:	
			if c - aux >= 0:
				arrRes.append(arr[c - aux])
			else:
				arrRes.append(0)
		else:
			if i == c:
				arrRes.append(arr[i])
			else:
				if c + aux < n:
					arrRes.append(arr[c + aux])
				else:
					arrRes.append(0)
		i = i + 1
	return arrRes

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _secuencia1 = request.form['secuencia1']
    _secuencia2 = request.form['secuencia2']
    cero1=[]
    cero2=[]
    ceroR=0
 
    i=0
 
    # validate the received values
    if _secuencia1 and _secuencia2:
        secuencia1 = _secuencia1.split(",")
        for s1 in secuencia1:
        	if not isNumber(s1):
        		c = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s1)
        		cero1=[i,c[0]]
        	i=i+1
    		
    	i=0
        secuencia2 = _secuencia2.split(",")
        for s2 in secuencia2:
        	if not isNumber(s2):
        		c = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s2)
        		cero2=[i,c[0]]
        	i=i+1

        if cero1[0]>cero2[0]:
        	ceroR=cero1[0]-cero2[0]

        	if len(secuencia1)>len(secuencia2):
        		auxLen = len(secuencia1)
        	else:
        		auxLen = (len(secuencia2)-cero2[0])+cero1[0]
        	
        	su = suma(secuencia1,secuencia2,cero1,cero2,auxLen)
        	mult = multi(secuencia1,secuencia2,cero1,cero2,auxLen)



        else:
        	ceroR=cero2[0]-cero1[0]

        	if len(secuencia2)>len(secuencia1):
        		auxLen = len(secuencia2)
        	else:
        		auxLen = (len(secuencia1)-cero1[0])+cero2[0]

        	su = suma(secuencia2,secuencia1,cero2,cero1,auxLen)
        	mult = multi(secuencia2,secuencia1,cero2,cero1,auxLen)
        
        div1 = division(secuencia1,secuencia2,cero1,cero2,auxLen)
        div2 = division(secuencia2,secuencia1,cero2,cero1,auxLen)
        rest1 = resta(secuencia1,secuencia2,cero1,cero2,auxLen)
        rest2 = resta(secuencia2,secuencia1,cero2,cero1,auxLen)
        refl1 = swap(secuencia1)
        refl2 = swap(secuencia2)


        
        



        

        #for s2 in secuencia2:
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()