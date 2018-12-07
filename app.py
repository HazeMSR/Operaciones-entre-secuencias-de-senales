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

def amplificar(arr,amp):
	aux = 0
	ret = []
	n =len(arr)
	i = 0

	while i < n:
		ret.append(float(arr[i])*amp)
		i = i + 1

	return ret

#Donde arr1 y arr2 son arrays, c1 y c2 son los ceros donde comienza cada array y n es la veces que se realizara la suma
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

#Donde arr1 y arr2 son arrays, c1 y c2 son los ceros donde comienza cada array y n es la veces que se realizara la suma
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
			arrRes.append(0)
		else:
			if r < 0:
				if i < rAbs:
					arrRes.append(0)
				else:
					if i-rAbs < arrLen1:
						arrRes.append(float(arr1[i-rAbs])/float(arr2[i]))
					else:
						arrRes.append(0)
			else:
				if i < arrLen1 and i-rAbs < arrLen2:
					arrRes.append(float(arr1[i])/float(arr2[i-rAbs]))
				else:
					arrRes.append(float(0))
		i=i+1
	return arrRes

def desplazar(arr,d):
	i = 0
	ret = [float(a) for a in arr]
	if d > 0:
		while i < d:
			ret.append(0)
			i = i + 1
	else:
		while i > d:
			ret.insert(0,0)
			i = i - 1
	return ret

def diezmar(arr,c,d):
	i = 0
	n = len(arr)
	arrRes = []
	aux = 0
	while i < n:
		aux = d*i
		if i < c:	
			if c - aux > 0:
				arrRes.append(float(arr[c - int(aux)]))
			else:
				arrRes.append(0)
		else:
			if i == c:
				arrRes.append(float(arr[i]))
			else:
				if c + aux < n:
					arrRes.append(float(arr[c + int(aux)]))
				else:
					arrRes.append(0)
		i = i + 1
	return arrRes
def convolucionar(arr1,arr2):
	cLen = len(arr1) + len(arr2) - 1
	auxLen1 = 0
	res = []
	conv = []
	aux = []
	whileAux = 0
	i = 0
	j = 0


	for a in arr1:
		aux = []
		for b in arr2:
			aux.append(float(a)*float(b))
		conv.append(aux)

	auxLen1 = len(conv)
	while i < cLen:

		whileAux = 0
		j = 0
		while j <= i:
			if j < auxLen1:
				if i-j < len(conv[j]):
					whileAux += conv[j][i-j]
			j += 1

		res.append(whileAux)
		i += 1
	return res
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
	_amp = request.form['amp']
	_desp = request.form['desp']
	_diezmar = request.form['diezmar']
	_interp = request.form['interp']

	cero1=[]
	cero2=[]
	su = []
	mult = []
	ceroR=0
	auxLen=0
	ceroAux=0
	i=0
 
	# validate the received values
	if _secuencia1 and _secuencia2:
		i=0
		secuencia2 = _secuencia2.split(",")
		secuencia1 = _secuencia1.split(",")
		sLen1 = len(secuencia1)
		sLen2 = len(secuencia2)
		for s1 in secuencia1:
			if not isNumber(s1):
				c = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s1)
				secuencia1[i]=c[0]
				cero1=[i,c[0]]
			i=i+1
				
		i=0
		for s2 in secuencia2:
			if not isNumber(s2):
				c = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s2)
				secuencia2[i]=c[0]
				cero2=[i,c[0]]
			i=i+1

		if len(cero1) > 0 and len(cero2) > 0:
			if cero1[0]>cero2[0]:
				ceroR=cero1[0]-cero2[0]
	
				if sLen1>sLen2:
					auxLen = sLen1
				else:
					auxLen = (sLen2-cero2[0])+cero1[0]
				
				su = suma(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
				mult = multi(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
	
			else:
				ceroR=cero2[0]-cero1[0]
	
				if sLen2>sLen1:
					auxLen = sLen2
				else:
					auxLen = (sLen1-cero1[0])+cero2[0]
	
				su = suma(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)
				mult = multi(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)

			
			div1 = division(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
			div2 = division(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)
			rest1 = resta(secuencia1,secuencia2,cero1[0],cero2[0],auxLen)
			rest2 = resta(secuencia2,secuencia1,cero2[0],cero1[0],auxLen)

			amp1 = amplificar(secuencia1,float(_amp))
			amp2 = amplificar(secuencia2,float(_amp))
			desp1 = desplazar(secuencia1,float(_desp))
			desp2 = desplazar(secuencia2,float(_desp))
			diez1 = diezmar(secuencia1,cero1[0],float(_diezmar))
			diez2 = diezmar(secuencia2,cero2[0],float(_diezmar))
			conv = convolucionar(secuencia1,secuencia2)

			#NO PONER NINGUNA FUNCION DEBAJO DEL REFLEJO
			refl1 = swap(secuencia1)
			refl2 = swap(secuencia2)
			

			#Saca los valores del eje x
			x = []
			x1 = []
			x2 = []
			xC = []
			i = 0

			for elem in secuencia1:
				x1.append(i-cero1[0])
				i = i+1
			i = 0
			for elem in secuencia2:
				x2.append(i-cero2[0])
				i = i+1

			i = 0
			ceroConv = cero1[0]+cero2[0]
			for elem in conv:
				xC.append(i-ceroConv)
				i = i+1

			if sLen1 > sLen2:
				ceroAux = cero1[0]
				x = x1
			else:
				ceroAux = cero2[0]
				x = x2


			secuencia1 = [float(a) for a in secuencia1]
			secuencia2 = [float(a) for a in secuencia2]
			refl1 = [float(a) for a in refl1]
			refl2 = [float(a) for a in refl2]
			return json.dumps({'grafica1':[cero1[0],secuencia1,x1],'grafica2':[cero2[0],secuencia2,x2],'suma':[ceroAux,su,x],'multiplicacion':[ceroAux,mult,x],'division1':[ceroAux,div1,x],'division2':[ceroAux,div2,x],'resta1':[ceroAux,rest1,x],'resta2':[ceroAux,rest2,x],"reflejo1":[cero1[0],refl1,x1],"reflejo2":[cero2[0],refl2,x2],"amplificacion1":[cero1[0],amp1,x1],"amplificacion2":[cero2[0],amp2,x2],"desplazamiento1":[ceroAux,amp1,x1],"desplazamiento2":[cero2[0],amp2,x2],"desplazamiento1":[cero1[0],desp1,x1],"desplazamiento2":[cero2[0],desp2,x2],"diezmacion1":[cero1[0],diez1,x1],"diezmacion2":[cero2[0],diez2,x2],"convolucion":[ceroConv,conv,xC]}) 
		else:
			return json.dumps({'html':'No ingreso ceros'})
	else:
		return json.dumps({'html':'No ingreso todos los campos'})

if __name__ == "__main__":
    app.run()