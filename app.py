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
	arrLen1 = len(arr1)
	arrLen2 = len(arr2)
	while i<n:
		if i < r:
			arrRes.append(float(arr1[i]))
		else:
			if i < arrLen1 and i-r < arrLen2:
				
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

	while i<n:
		if i < r:
			arrRes.append(float(arr1[i]))
		else:
			if r < 0:
				if i < rAbs:
					arrRes.append(float(arr2[i])*(-1))
				else:
					if i-rAbs < arrLen1:
						arrRes.append(float(arr1[i-rAbs])-float(arr2[i]))
					else:
						arrRes.append(float(arr2[i])*(-1))
			else:
				if i < arrLen1 and i-rAbs < arrLen2:
					arrRes.append(float(arr1[i])-float(arr2[i-rAbs]))
				else:
					if i >= arrLen2:
						arrRes.append(float(arr1[i]))
					else:
						arrRes.append(float(arr2[i-rAbs])*(-1))
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
			arrRes.append(float(0))
		else:
			if i < arrLen1 and i-r < arrLen2:
				arrRes.append(float(arr1[i])*float(arr2[i-r]))
			else:
				arrRes.append(float(0))
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
	aux=0

	while i<n:
		if i < r:
			print("if1  "+str(i)+" < "+str(r))
			print("i = "+str(i))
			print("arr1[i] = "+str(arr1[i]))
			arrRes.append(0)
		else:
			print("else 1er if")
			if r < 0:
				print("if2  "+str(r)+" < "+str(0))
				if i < rAbs:
					print("if3 " +str(i)+" < "+str(rAbs))
					arrRes.append(0)
				else:
					print("else 3er if")
					print("i = "+str(i))
					print("r = "+str(rAbs))
					if i-rAbs < arrLen1:
						arrRes.append(float(arr1[i-rAbs])/float(arr2[i]))
					else:
						arrRes.append(0)
			else:
				print("else 2do if")
				if i < arrLen1 and i-rAbs < arrLen2:
					print("if4 "+str(i)+" < "+str(arrLen1)+" and "+str(i-rAbs)+" < "+str(arrLen2))
					print("i = "+str(i))
					print("r = "+str(rAbs))
					print("arr1[i] = "+str(arr1[i]))
					print("arr2[i-r] = "+str(arr2[i-rAbs]))
					arrRes.append(float(arr1[i])/float(arr2[i-rAbs]))
				else:
					print("else 4to if")
					print("i = "+str(i))
					print("r = "+str(rAbs))
					arrRes.append(float(0))
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
	su = []
	mult = []
	ceroR=0
	auxLen=0
 
	i=0
 
	# validate the received values
	if _secuencia1 and _secuencia2:
		secuencia1 = _secuencia1.split(",")
		for s1 in secuencia1:
			if not isNumber(s1):
				c = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s1)
				secuencia1[i]=c[0]
				cero1=[i,c[0]]
			i=i+1
				
		i=0
		secuencia2 = _secuencia2.split(",")
		for s2 in secuencia2:
			if not isNumber(s2):
				c = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s2)
				secuencia2[i]=c[0]
				cero2=[i,c[0]]
			i=i+1

		if len(cero1) > 0 and len(cero2) > 0:
			if cero1[0]>cero2[0]:
				ceroR=cero1[0]-cero2[0]
	
				if len(secuencia1)>len(secuencia2):
					auxLen = len(secuencia1)
				else:
					auxLen = (len(secuencia2)-cero2[0])+cero1[0]
				
				su = suma(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
				mult = multi(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
	
			else:
				ceroR=cero2[0]-cero1[0]
	
				if len(secuencia2)>len(secuencia1):
					auxLen = len(secuencia2)
				else:
					auxLen = (len(secuencia1)-cero1[0])+cero2[0]
	
				su = suma(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)
				mult = multi(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)
			
			su = [str(i) for i in su]
			mult = [str(i) for i in mult]
			div1 = division(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
			div1 = [str(i) for i in div1]
			div2 = division(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)
			div2 = [str(i) for i in div2]
			rest1 = resta(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
			rest1 = [str(i) for i in rest1]
			rest2 = resta(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)
			rest2 = [str(i) for i in rest2]
			refl1 = swap(secuencia1)
			refl1 = [str(i) for i in refl1]
			refl2 = swap(secuencia2)
			refl1 = [str(i) for i in refl1]
	
			return json.dumps({'suma':su,'multiplicacion':mult,'division1':div1,'division2':div2,'resta1':rest1,'resta2':rest2,"reflejo1":refl1,"reflejo2":refl2}) 
		else:
			return json.dumps({'html':'<span>No ingreso ceros</span>'})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()