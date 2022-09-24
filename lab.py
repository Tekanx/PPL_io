
# Numpy es una librería utilizada para el trabajo multi-dimensional de arreglos de Python-
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def packComponents():
    input_r1_x.pack()
    input_r1_y.pack()
    input_r2_x.pack()
    input_r2_y.pack()
    input_r3_x.pack()
    input_r3_y.pack()
    input_r4_x.pack()
    input_r4_y.pack()
    input_r5_x.pack()
    input_r5_y.pack()
    labelRestriccion1.pack()
    labelRestriccion2.pack()
    labelRestriccion3.pack()
    labelRestriccion4.pack()
    labelRestriccion5.pack()
    r1_simbol1.pack()
    r2_simbol2.pack()
    r3_simbol3.pack()
    r4_simbol4.pack()
    r5_simbol5.pack()
    input_r1_res.pack()
    comboBox_r1_cond.pack()
    input_r2_res.pack()
    comboBox_r2_cond.pack()
    input_r3_res.pack()
    comboBox_r3_cond.pack()
    input_r4_res.pack()
    comboBox_r4_cond.pack()
    input_r5_res.pack()
    comboBox_r5_cond.pack()   
    
def unpackComponents():
    labelRestriccion1.pack_forget()
    labelRestriccion2.pack_forget()
    labelRestriccion3.pack_forget()
    labelRestriccion4.pack_forget()
    labelRestriccion5.pack_forget()
    input_r1_x.pack_forget()
    input_r1_y.pack_forget()
    input_r2_x.pack_forget()
    input_r2_y.pack_forget()
    input_r3_x.pack_forget()
    input_r3_y.pack_forget()
    input_r4_x.pack_forget()
    input_r4_y.pack_forget()
    input_r5_x.pack_forget()
    input_r5_y.pack_forget()
    r1_simbol1.pack_forget()
    r2_simbol2.pack_forget()
    r3_simbol3.pack_forget()
    r4_simbol4.pack_forget()
    r5_simbol5.pack_forget()
    input_r1_res.pack_forget()
    comboBox_r1_cond.pack_forget()
    input_r2_res.pack_forget()
    comboBox_r2_cond.pack_forget()
    input_r3_res.pack_forget()
    comboBox_r3_cond.pack_forget()
    input_r4_res.pack_forget()
    comboBox_r4_cond.pack_forget()
    input_r5_res.pack_forget()
    comboBox_r5_cond.pack_forget()   
        
def RenderRestricciones():
    packComponents()
    if (cantRes.get() == ''):
        print('ERROR!')
        unpackComponents()
    else:
        if(int(cantRes.get()) == 1):
            labelRestriccion1.place(x=300, y= 130)
            input_r1_x.pack()
            input_r1_y.pack()
            labelRestriccion2.pack_forget()
            labelRestriccion3.pack_forget()
            labelRestriccion4.pack_forget()
            labelRestriccion5.pack_forget()
            input_r1_x.place(x=380, y= 130, width=20)
            input_r1_y.place(x=450, y= 130, width=20)
            input_r2_x.pack_forget()
            input_r2_y.pack_forget()
            input_r3_x.pack_forget()
            input_r3_y.pack_forget()
            input_r4_x.pack_forget()
            input_r4_y.pack_forget()
            input_r5_x.pack_forget()
            input_r5_y.pack_forget()
            r2_simbol2.pack_forget()
            r3_simbol3.pack_forget()
            r4_simbol4.pack_forget()
            r5_simbol5.pack_forget()
            r1_simbol1.place(x=415, y=130) 
            comboBox_r1_cond.place(x=480, y=130)   
            input_r1_res.place(x=550, y=130, width=20)
            
            input_r2_res.pack_forget()
            comboBox_r2_cond.pack_forget()
            input_r3_res.pack_forget()
            comboBox_r3_cond.pack_forget()
            input_r4_res.pack_forget()
            comboBox_r4_cond.pack_forget()
            input_r5_res.pack_forget()
            comboBox_r5_cond.pack_forget()       
        elif(int(cantRes.get()) == 2):
            labelRestriccion1.place(x=300, y= 130)
            labelRestriccion2.place(x=300, y= 150)
            labelRestriccion3.pack_forget()
            labelRestriccion4.pack_forget()
            labelRestriccion5.pack_forget()
            input_r1_x.place(x=380, y= 130, width=20)
            input_r1_y.place(x=450, y= 130, width=20)
            input_r2_x.place(x=380, y= 150, width=20)
            input_r2_y.place(x=450, y= 150, width=20)
            input_r3_x.pack_forget()
            input_r3_y.pack_forget()
            input_r4_x.pack_forget()
            input_r4_y.pack_forget()
            input_r5_x.pack_forget()
            input_r5_y.pack_forget()
            r3_simbol3.pack_forget()
            r4_simbol4.pack_forget()
            r5_simbol5.pack_forget()
            r1_simbol1.place(x=415, y=130)
            r2_simbol2.place(x=415, y=150)
            input_r2_res.pack_forget()
            comboBox_r2_cond.pack_forget()
            input_r3_res.pack_forget()
            comboBox_r3_cond.pack_forget()
            input_r4_res.pack_forget()
            comboBox_r4_cond.pack_forget()
            input_r5_res.pack_forget()
            comboBox_r5_cond.pack_forget()
            comboBox_r1_cond.place(x=480, y=130)
            input_r1_res.place(x=550, y=130, width=20)
            comboBox_r2_cond.place(x=480, y=150)
            input_r2_res.place(x=550, y=150, width=20)
        elif(int(cantRes.get()) == 3):
            labelRestriccion1.place(x=300, y= 130)
            labelRestriccion2.place(x=300, y= 150)
            labelRestriccion3.place(x=300, y= 170)
            labelRestriccion4.pack_forget()
            labelRestriccion5.pack_forget()
            input_r1_x.place(x=380, y= 130, width=20)
            input_r1_y.place(x=450, y= 130, width=20)
            input_r2_x.place(x=380, y= 150, width=20)
            input_r2_y.place(x=450, y= 150, width=20)
            input_r3_x.place(x=380, y= 170, width=20)
            input_r3_y.place(x=450, y= 170, width=20)
            input_r4_x.pack_forget()
            input_r4_y.pack_forget()
            input_r5_x.pack_forget()
            input_r5_y.pack_forget()
            r4_simbol4.pack_forget()
            r5_simbol5.pack_forget()    
            r1_simbol1.place(x=415, y=130)
            r2_simbol2.place(x=415, y=150)
            r3_simbol3.place(x=415, y=170)
            input_r4_res.pack_forget()
            comboBox_r4_cond.pack_forget()
            input_r5_res.pack_forget()
            comboBox_r5_cond.pack_forget()
            comboBox_r1_cond.place(x=480, y=130)
            input_r1_res.place(x=550, y=130, width=20)
            comboBox_r2_cond.place(x=480, y=150)
            input_r2_res.place(x=550, y=150, width=20)
            comboBox_r3_cond.place(x=480, y=170)
            input_r3_res.place(x=550, y=170, width=20)
        elif(int(cantRes.get()) == 4):
            labelRestriccion1.place(x=300, y= 130)
            labelRestriccion2.place(x=300, y= 150)
            labelRestriccion3.place(x=300, y= 170)
            labelRestriccion4.place(x=300, y= 190)
            labelRestriccion5.pack_forget()
            input_r1_x.place(x=380, y= 130, width=20)
            input_r1_y.place(x=450, y= 130, width=20)
            input_r2_x.place(x=380, y= 150, width=20)
            input_r2_y.place(x=450, y= 150, width=20)
            input_r3_x.place(x=380, y= 170, width=20)
            input_r3_y.place(x=450, y= 170, width=20)
            input_r4_x.place(x=380, y= 190, width=20)
            input_r4_y.place(x=450, y= 190, width=20)
            input_r5_x.pack_forget()
            input_r5_y.pack_forget()
            r5_simbol5.pack_forget()    
            r1_simbol1.place(x=415, y=130)
            r2_simbol2.place(x=415, y=150)
            r3_simbol3.place(x=415, y=170)
            r4_simbol4.place(x=415, y=190)
            input_r5_res.pack_forget()
            comboBox_r5_cond.pack_forget()
            
            comboBox_r1_cond.place(x=480, y=130)
            input_r1_res.place(x=550, y=130, width=20)
            comboBox_r2_cond.place(x=480, y=150)
            input_r2_res.place(x=550, y=150, width=20)
            comboBox_r3_cond.place(x=480, y=170)
            input_r3_res.place(x=550, y=170, width=20)
            comboBox_r4_cond.place(x=480, y=190)
            input_r4_res.place(x=550, y=190, width=20)
        elif(int(cantRes.get()) == 5):
            labelRestriccion1.place(x=300, y= 130)
            labelRestriccion2.place(x=300, y= 150)
            labelRestriccion3.place(x=300, y= 170)
            labelRestriccion4.place(x=300, y= 190)
            labelRestriccion5.place(x=300, y= 210)
            input_r1_x.place(x=380, y= 130, width=20)
            input_r1_y.place(x=450, y= 130, width=20)
            input_r2_x.place(x=380, y= 150, width=20)
            input_r2_y.place(x=450, y= 150, width=20)
            input_r3_x.place(x=380, y= 170, width=20)
            input_r3_y.place(x=450, y= 170, width=20)
            input_r4_x.place(x=380, y= 190, width=20)
            input_r4_y.place(x=450, y= 190, width=20)
            input_r5_x.place(x=380, y= 210, width=20)
            input_r5_y.place(x=450, y= 210, width=20)    
            r1_simbol1.place(x=415, y=130)
            r2_simbol2.place(x=415, y=150)
            r3_simbol3.place(x=415, y=170)
            r4_simbol4.place(x=415, y=190)
            r5_simbol5.place(x=415, y=210)
            comboBox_r1_cond.place(x=480, y=130)
            input_r1_res.place(x=550, y=130, width=20)
            comboBox_r2_cond.place(x=480, y=150)
            input_r2_res.place(x=550, y=150, width=20)
            comboBox_r3_cond.place(x=480, y=170)
            input_r3_res.place(x=550, y=170, width=20)
            comboBox_r4_cond.place(x=480, y=190)
            input_r4_res.place(x=550, y=190, width=20)
            comboBox_r5_cond.place(x=480, y=210)
            input_r5_res.place(x=550, y=210, width=20)
        else: 
            print('ERROR!')
            unpackComponents() 

#Funcion despejar restricciones
def despejar_ecc(REST):
    d=[]
    #Si X es cero
    if (int(REST[0]==0)):
        desp_y = (REST[3])/int(REST[1])
        d.append(0)
        d.append(desp_y)
    else:
        #Si Y es cero
        if (int(REST[1])==0): 
            desp_x = (REST[3])/int(REST[1])
            d.append(0)
            d.append(desp_x)
        else: #Ninguna es cero
            desp_x=int(REST[3])/int(REST[0]) #PRIMERO SE IGUALA X=0 PARA OBTENER Y
            d.append(desp_x)
            desp_y=int(REST[3])/int(REST[1]) #SE REALIZA LO MISMO EN Y PARA OBTENER X
            d.append(desp_y)
        return d

"""""""
def despejar (restriccion1,restriccion2):
    interseccion=[]
"""

def Solver():
    print('AAAAAAAAAAAAAAA CONCHETUMARE')
    #Definir atributos
    var_opcion=min_max.get()
    X=var_x.get()
    Y=var_y.get()
    #Cuenta restricciones
    Cont_R=0 
    
    #Arreglos para restricciones??
    REST_1=[]
    REST_2=[]
    REST_3=[]
    REST_4=[]
    REST_5=[]
    
    #Recibir parámetros
    if var_opcion == '' or X == '' or Y == '':
        print("Esta vacío :)")
    else:
        var_opcion=min_max.get()
        X=int(var_x.get())
        Y=int(var_y.get())
    #Se guarda la 1° restricción
    if (r1_x.get()=='' and r1_y.get()==''):
        print("Esta vacío :)")
    else: 
        if (r1_x.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r1_x.get())

        if (r1_y.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r1_y.get())
            #FALTAN 2 VARIABLES
        Cont_R=Cont_R+1      
        
    #Se guarda la 2° restricción
    if (r2_x.get()=='' and r2_y.get()==''):
        print("Esta vacío :)")
    else: 
        if (r2_x.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r2_x.get())

        if (r2_y.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r2_y.get())
            #FALTAN 2 VARIABLES
        Cont_R=Cont_R+1  

    #Se guarda la 3° restricción
    if (r3_x.get()=='' and r3_y.get()==''):
        print("Esta vacío :)")
    else: 
        if (r3_x.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r3_x.get())

        if (r3_y.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r3_y.get())
            #FALTAN 2 VARIABLES
        Cont_R=Cont_R+1 

    #Se guarda la 4° restricción
    if (r4_x.get()=='' and r4_y.get()==''):
        print("Esta vacío :)")
    else: 
        if (r4_x.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r4_x.get())

        if (r4_y.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r4_y.get())
            #FALTAN 2 VARIABLES
        Cont_R=Cont_R+1 

    #Se guarda la 5° restricción
    if (r5_x.get()=='' and r5_y.get()==''):
        print("Esta vacío :)")
    else: 
        if (r5_x.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r5_x.get())

        if (r5_y.get==''):
            REST_1.append(0)
        else: 
            REST_1.append(r5_y.get())
            #FALTAN 2 VARIABLES
        Cont_R=Cont_R+1 

    #Se buscan las intersecciones de x e y para las restricciones
    #LA VDD NO SE QUE HICE#
    if(Cont_R==1):
        despejar_ecc(REST_1)
    else:
        if(Cont_R==2):
            despejar_ecc(REST_1)
            despejar_ecc(REST_2)
        else:
            if(Cont_R==3):
                despejar_ecc(REST_1)
                despejar_ecc(REST_2)
                despejar_ecc(REST_3)
            else:
                if(Cont_R==4):
                    despejar_ecc(REST_1)
                    despejar_ecc(REST_2)
                    despejar_ecc(REST_3)
                    despejar_ecc(REST_4)
                else:
                    if(Cont_R==5):
                        despejar_ecc(REST_1)
                        despejar_ecc(REST_2)
                        despejar_ecc(REST_3)
                        despejar_ecc(REST_4)
                        despejar_ecc(REST_5)
                    else:
                        print("Error")


    #Se busca el conjunto de soluciones
    conjunto_solucion = []
    #CREAR FUNCION
    #Sector generación gráfico del conjunto de soluciónif(conjunto_solucion):
    if(conjunto_solucion):
        graph = plt.subplot()
        R_1 = []
        R_2 = []
        R_3 = []
        R_4 = []
        R_5 = []
        
        #Graficar Restriccion n°1
        X1 = []
        Y1 = []
        if(int(REST_1[1]) == 0):
            print()
        
        #Graficar Restriccion n°2
        
        #Graficar Restriccion n°3
        if(Cont_R == 3):
            print('3 restricciones ctm')
            X3 = []
            Y3 = []
        #Graficar Restriccion n°4
        elif(Cont_R == 4):
            print('4 restricciones ctm')
            X4 = []
            Y4 = []
        
        #Graficar Restriccion n°5
        elif(Cont_R == 5):
            print('5 restricciones ctm')
            X5 = []
            Y5 = []
            
        #Se genera funcion objetivo Z
        Z = []
        Z.append(X)
        Z.append('+')
        Z.append(Y)
        Z.append('+')
        Z.append('k')
        #Graficar curva de nivel de la funcion objetivo
        curva_X1 = []
        curva_Y1 = []
        for k in range(300, 1000, 200):
            print('')
    else:
        print('Espacio infactible!')
    

#Sector minimizar / maximizar
frame = Tk()
frame.title("PPL")
frame.geometry("1000x520")
min_max = StringVar()
opcion = ttk.Combobox(frame, width=20,textvariable=min_max)
opcion.place(x=30, y=50)
opcion['values'] = ['Minimizar', 'Maximizar']
labelOpcion = Label(frame, text='Seleccione una opcion: ')
labelOpcion.place(x=30, y=25)

titulo = Label(frame, text = "Laboratorio n°1: PPL")
titulo.pack(anchor=CENTER)

#Sector variables de decisión
labelVariables = Label(frame, text='Ingrese variables de decisión')
labelVariables.place(x=30,y=100)
labelx = Label(frame, text='X: ')
labely = Label(frame,text='Y: ')
labelx.place(x=30, y=125)
labely.place(x=30, y=150)
var_x = StringVar()
inputx = Entry(frame, textvariable=var_x)
inputx.place(x=50, y=125)
var_y = StringVar()
inputy = Entry(frame, textvariable=var_y)
inputy.place(x=50, y=150)

#Sector restricciones
labelRestricciones = Label(frame, text='Restricciones')
labelRestricciones.place(x=300, y=70)
cantRes = StringVar()
comboBoxCantRes =  ttk.Combobox(frame, width=5, textvariable=cantRes)
comboBoxCantRes["values"] = [1, 2, 3, 4, 5]
comboBoxCantRes.place(x=300, y=100)


labelRestriccion1 = Label(frame, text="Restricción 1")
r1_x = StringVar()
input_r1_x = Entry(frame, textvariable=r1_x)
r1_y = StringVar()
input_r1_y = Entry(frame, textvariable=r1_y)
r1_simbol1 = Label(frame,text="+")

labelRestriccion2 = Label(frame, text="Restricción 2")
r2_x = StringVar()
input_r2_x = Entry(frame, textvariable=r2_x)
r2_y = StringVar()
input_r2_y = Entry(frame, textvariable=r2_y)
r2_simbol2 = Label(frame,text="+")

labelRestriccion3 = Label(frame, text="Restricción 3")
r3_x = StringVar()
input_r3_x = Entry(frame, textvariable=r3_x)
r3_y = StringVar()
input_r3_y = Entry(frame, textvariable=r3_y)
r3_simbol3 = Label(frame,text="+")

labelRestriccion4 = Label(frame, text="Restricción 4")
r4_x = StringVar()
input_r4_x = Entry(frame, textvariable=r4_x)
r4_y = StringVar()
input_r4_y = Entry(frame, textvariable=r4_y)
r4_simbol4 = Label(frame,text="+")

labelRestriccion5 = Label(frame, text="Restricción 5")
r5_x = StringVar()
input_r5_x = Entry(frame, textvariable=r5_x)
r5_y = StringVar()
input_r5_y = Entry(frame, textvariable=r5_y)
r5_simbol5 = Label(frame,text="+")

var_r1_res = StringVar()
input_r1_res = Entry(frame, textvariable=var_r1_res)
var_r1_cond = StringVar()
comboBox_r1_cond = ttk.Combobox(frame, width=5, textvariable=var_r1_cond)
comboBox_r1_cond["values"]=["<=","=",">="]
var_r2_res = StringVar()
input_r2_res = Entry(frame, textvariable=var_r2_res)
var_r2_cond = StringVar()
comboBox_r2_cond = ttk.Combobox(frame, width=5, textvariable=var_r2_cond)
comboBox_r2_cond["values"]=["<=","=",">="]
var_r3_res = StringVar()
input_r3_res = Entry(frame, textvariable=var_r3_res)
var_r3_cond = StringVar()
comboBox_r3_cond = ttk.Combobox(frame, width=5, textvariable=var_r3_cond)
comboBox_r3_cond["values"]=["<=","=",">="]
var_r4_res = StringVar()
input_r4_res = Entry(frame, textvariable=var_r4_res)
var_r4_cond = StringVar()
comboBox_r4_cond = ttk.Combobox(frame, width=5, textvariable=var_r4_cond)
comboBox_r4_cond["values"]=["<=","=",">="]
var_r5_res = StringVar()
input_r5_res = Entry(frame, textvariable=var_r5_res)
var_r5_cond = StringVar()
comboBox_r5_cond = ttk.Combobox(frame, width=5, textvariable=var_r5_cond)
comboBox_r5_cond["values"]=["<=","=",">="]

buttonCantRes = ttk.Button(text="Seleccionar cantidad de restricciones", command=RenderRestricciones)
buttonCantRes.place(x=360, y=100)
buttonResolver = ttk.Button(text='Resolver PPL', command=Solver)
buttonResolver.place(x=50, y=200, width=140)

frame.mainloop()