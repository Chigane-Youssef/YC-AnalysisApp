# -*- coding: utf-8 -*-
""" @author: CHIGANE Youssef """

 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import filedialog,ttk,messagebox
from PIL import ImageTk
import concurrent.futures
from win32api import GetSystemMetrics
import random

### Importation de données
def read_data(path):   

    ### Lire le fichier et affecter le data à une variable
    
    if path[-3:] == "sav":
        try : 
            data = pd.read_spss(path)
        except:
            messagebox.showerror("Erreur","Veuillez vérifier le fichier .sav",parent=root)
                                
    elif path[-4:-1] == "xls":
        try :
            data = pd.read_excel(path)
        except:
            messagebox.showerror("Erreur","Veuillez vérifier le fichier .sav",parent=root)
    else:
        try :
            data = pd.read_csv(path)
        except:
            messagebox.showerror("Erreur","Veuillez vérifier le fichier choisit",parent=root)

    
    return data
## Fonction pour générer des graphes

def basic_graph(ax,datax,datay,parametres):
    """Fonction pour graphe simple"""
    
    return ax.plot(datax,datay,**parametres)

def bar_chart(bars,labels,values):
    """Fonction pour graphe bar"""
    
    return bars.bar(labels,values)

def line_graph(axs,datax,datay,parametres):
    """Fonction pour graphe courbe"""
    
    return axs.plot(datax,datay,**parametres)

def histogram(axs,bins,data,parametres):
    """Fonction pour histograme"""
    
    return axs.hist(data, bins=bins,**parametres)

def pie_chart(axs,labels,data,parametres):
    """Fonction pour diagramme circulaire"""
    
    return axs.pie(data,labels=labels,**parametres)

def box_plot(axs,data,labels):
    """Fonction pour boite à moustache"""
    
    return axs.boxplot(data,labels)


def grouped_bar_chart(axs,labels,data,data_labels,parametres):
    x = np.arange(len(labels))  
    width = 1-0.4*len(labels)

    for i in range(len(data)):
        if i==0:
            axs.bar(x , data[i], width)
        elif i%2==0:
            axs.bar(x - ((-1)**i) * int(np.floor(i)) * width/2, data[i], width)
        else:
            axs.bar(x - ((-1)**i) * (int(np.floor(i))+1) * width/2, data[i], width)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    
#Classe pour le login

class Login:
    """classe pour la fenêtre de login"""
    
    def __init__(self, master):
        
        #Ajout de image de background
        self.bg = ImageTk.PhotoImage(file = "login_img1.jpg")
        
        #personalisation de fenêtre Login
        master.title("Login")
        master.iconbitmap("lock.ico")
        master.geometry("1000x500")
        master.minsize(720,600)
        self.bg_img = Label(master, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #Entry variables
        self.user = StringVar()
        self.password = StringVar()
        
        #Frame login
        self.frame = Frame(master, bg="white",relief=GROOVE,borderwidth=2).\
                    place(x=100,y=200,height=200,width=350)
        self.tilte = Label(self.frame,text="Login:",font=("Impact",20,"bold"),fg="#d77337",bg="white").\
                    place(x=110,y=210)
        self.user_label = Label(self.frame,text="Username",font=("Courrier",13,"bold"),fg="gray",bg="white").\
                    place(x=110,y=260)
        self.password_label = Label(self.frame,text="Password",font=("Courrier",13,"bold"),fg="gray",bg="white").\
                    place(x=110,y=320)
        self.user_entry = Entry(self.frame,textvariable=self.user,font=("times new roman",13),bg="#F5E9E6").\
                    place(x=112,y=280)
        self.password_entry = Entry(self.frame,textvariable=self.password,font=("times new roman",13),bg="#F5E9E6",show="*").\
                    place(x=112,y=340)
        self.log_button = Button(self.frame,text="Login",fg="white",bg="#d77337",font=("times new roman",13),command=self.login).\
                    place(x=220,y=383,width=100)
        
    def login(self):
        """Fonction de vérification identifiants liée au boutton login"""
        
        if self.user.get()=="Admin" and self.password.get()=="Admin":
            root.quit #Quitter comme effet d'animation
            for item in root.winfo_children():# effacer la fenêtre login pour la réuitiliser à nouveau(en effacant les widget)
                item.destroy()
            
            HCP_Dashboard = DataVs(root)#Créer une nouvelle fenêtre pour Desktop app + utilisation de même root
            
        else : 
            messagebox.showinfo("Error","Login failed",parent=self.frame)
class DataVs:
    """Classe principale pour choisir l'action à exécuter """
    
    def __init__(self,master):
       
        #Ajout de image de background
        self.bg = ImageTk.PhotoImage(file = "login_img1.jpg")
        
        #personalisation de fenêtre HCP-ESI
        master.title("HCP-ESI Dashboards")
        master.geometry("1200x620")
        master.iconbitmap("hcp_esi_img.ico")
        self.bg_img = Label(master, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #Frame 1 pour affichage de texte
        self.frame1 = Frame(master)
        self.frame1.pack(padx=40,pady=10) 
        self.label1 = Label(self.frame1,text="Bienvenue à HCP-ESI App",font=("Cambria",23),borderwidth=1)\
                    .pack(fill=X,pady=10, padx=10)
        
        #Frame 2 pour les boutton
        self.frame2 = Frame(master, bg="white",relief=GROOVE,borderwidth=2)
        self.frame2.pack(fill=X,padx=20,pady=10) 
        self.label2 = Label(self.frame2,text="Que vous voulez faire ?",font=("Cambria",15,"bold"),borderwidth=1)\
                    .pack(fill=X,side=TOP,pady=10, padx=10)
        
        self.option1 = Button(self.frame2,text="Visualisation des données : Recensement générale de la population et de l'habitat",fg="white",bg="#d77337",font=("times new roman",25),command=self.option1).\
                    pack(fill=X,pady=10, padx=10)
        self.option2 = Button(self.frame2,text="Visualisation des données : Consommation et les Depenses des Menages",fg="white",bg="#d77337",font=("times new roman",25),command=self.option2).\
                    pack(fill=X,pady=10, padx=10)
        self.option3 = Button(self.frame2,text="Visualisation des données : Personaliser",fg="white",bg="#d77337",font=("times new roman",25),command=self.option3).\
                    pack(fill=X,pady=10, padx=10)
        self.option4 = Button(self.frame2,text="Convertir un fichier",fg="white",bg="#d77337",font=("times new roman",25),command=self.option4).\
                    pack(fill=X,pady=10, padx=10)
        
        #Boutton pour quitter
        self.exit_app = Button(master,text="Quitter",fg="white",bg="red",font=("times new roman",20),width=30,command=self.quitter).\
                    pack(side=BOTTOM)
        
    def quitter(self):
        """Fonction pour boutton quiter"""
        
        root.destroy()
        
    def option1(self):
        """Fonction pour la visualisation de data recensement population"""

        path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier de population",filetypes=(("Tous les fichiers","*.*"),("Fichier excel","*.xls"),("Fichier excel","*.xlsx"),("Fichier spss","*.sav"),("Fichier text","*.txt"),("Fichier csv","*.csv")))
        root.withdraw()
        
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            f1 = executor.submit(read_data,path)
            master = loading_win()
            master.update()
            try:
                data = f1.result()
            except:
                root.deiconify()
            master.destroy()


        path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")

        flag=True
        i=0
        while flag:
            try:
                i+=1
                open(path2+'/menages'+str(i)+'.pdf','r')
                print("Done")
            except:
                flag=False

        try:
            print(i)
            figure1 , ax1 = plt.subplots()
            dat = data["MIL"].value_counts().index.tolist()
            
            for _ in range(len(dat)):
                bar_chart()
                
            plt.xlabel('Milieu')
            plt.ylabel('Pourcentage')
            plt.title("Taux urbanisme")
            plt.legend()
            

                
            pdf = PdfPages(path2+'/menages'+str(i)+'.pdf')
            pdf.savefig( figure1 )
            pdf.close()
            messagebox.showinfo("Success","Opération terminée",parent=root)
            
            print(path2+'/menages'+str(i)+'.pdf')
            root.deiconify()
        except:
            root.deiconify()
            print(path2+'/menages'+str(i)+'.pdf')

        
    def option2(self):
        """Fonction pour la visualisation de data ménages"""
        
        path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier de population",filetypes=(("Tous les fichiers","*.*"),("Fichier excel","*.xls"),("Fichier excel","*.xlsx"),("Fichier spss","*.sav"),("Fichier text","*.txt"),("Fichier csv","*.csv")))
        root.withdraw()
        
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            f1 = executor.submit(read_data,path)
            master = loading_win()
            master.update()
            try:
                data = f1.result()
            except:
                root.deiconify()
            master.destroy()


        path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")

        flag=True
        i=0
        while flag:
            try:
                i+=1
                open(path2+'/menages'+str(i)+'.pdf','r')
                print("Done")
            except:
                flag=False
####Plots
        try:
            figure1 , ax1 = plt.subplots()
            data_lab = data["MIL"].value_counts().index.tolist()
            data_val = data["MIL"].value_counts().values.tolist()
            
            for _ in range(len(data_lab)):
                bar_chart(ax1,data_lab[_],data_val[_]/data["MIL"].count()*100)
                
            ax1.grid(b = True, color ='black',linestyle ='-.', linewidth = 0.5,alpha = 0.4)
            plt.xlabel('Milieu')
            plt.ylabel('Pourcentage %')
            plt.title("Taux urbanisme")
            
            figure2 , ax2 = plt.subplots()
            box_plot(ax2,data["TAILLE"],"Taille")
            ax2.grid(b = True, color ='black',linestyle ='-.', linewidth = 0.5,alpha = 0.4)
            plt.xlabel('Taille')
            plt.ylabel('Nbr')
            plt.title("Taille de ménage")
            
            data_lab = data["REG"].value_counts().index.tolist()
            data_val = data["REG"].value_counts().values.tolist()
            figure3 , ax3 = plt.subplots(figsize=(10,10))
            don = []
            for _ in range(len(data_val)):
                don.append(data_val[_])
            plt.pie(don, labels = data_lab,autopct='%.2f %%')
            plt.title("Régions")
            
            pdf = PdfPages(path2+'/menages'+str(i)+'.pdf')
            pdf.savefig( figure1 )
            pdf.savefig( figure2 )
            pdf.savefig( figure3 )
            pdf.close()
            
            messagebox.showinfo("Success","Opération terminée",parent=root)
            root.deiconify()
        except:
            root.deiconify()
            print("failed")

        
    def option3(self):
        ### Fenêtre de personnalisation
        
        path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier de population",filetypes=(("Tous les fichiers","*.*"),("Fichier excel","*.xls"),("Fichier excel","*.xlsx"),("Fichier spss","*.sav"),("Fichier text","*.txt"),("Fichier csv","*.csv")))
                
        with concurrent.futures.ThreadPoolExecutor() as executor:
            f1 = executor.submit(read_data,path)
            master = loading_win()
            master.update()
            try:
                data = f1.result()
            except:
                root.deiconify()
            master.destroy()
            self.all_data = data
        root.withdraw()
        root2=Tk()
        roo =Dashboard_maker(root2,data)
        root2.mainloop()


    def option4(self):
        """Fonction pour convertir les format .sav .csv .xls .xlsx"""
        

        
        root2 = Tk()
        root2.title("Convertir")
        root2.iconbitmap("hcp_esi_img.ico")
        root2.config(background="black")
        root2.geometry("500x500")
        root2.minsize(500,500)
        
        spss_excel = Button(root2,text="SPSS TO EXCEL", compound=LEFT,font=("times new roman",30),command=lambda : [Spss_excel(),root2.destroy()]).\
                    pack(fill=X,pady=10, padx=10)
        spss_csv = Button(root2,text="SPSS TO CSV", compound=LEFT,font=("times new roman",30),command=lambda : [Spss_csv(),root2.destroy()]).\
                    pack(fill=X,pady=10, padx=10)
        excel_csv = Button(root2,text="EXCEL TO CSV", compound=LEFT,font=("times new roman",30),command=lambda : [Excel_csv(),root2.destroy()]).\
                    pack(fill=X,pady=10, padx=10)
        csv_excel = Button(root2,text="CSV TO EXCEL", compound=LEFT,font=("times new roman",30),command=lambda : [Csv_excel(),root2.destroy()]).\
                    pack(fill=X,pady=10, padx=10)

        
        root2.mainloop()
class Dashboard_maker:
        def __init__(self,master,data):
            Width = GetSystemMetrics(0)
            Height = GetSystemMetrics(1) 
            master.title("Dashboard Maker")
            master.iconbitmap("hcp_esi_img.ico")
            master.geometry(str(int(Width*0.95))+"x"+str(int(Height*0.85)))
            master.resizable(height=False)
    ###frames
            frame1 = Frame(master, relief='raised', borderwidth=5,bg="black")
            frame1.pack(fill=X,padx=40,pady=10)

            self.frame2 = Frame(master, relief='raised', borderwidth=5,bg="gold")
            self.frame2.pack(fill=X,padx=40,pady=10)

            frame3 = LabelFrame(master, relief='raised', borderwidth=5)
            frame3.pack(expand=True)

    ####Vars
            self.all_data=data
#             self.graphs = []
#             self.datax = StringVar()
#             self.datay = StringVar()
#             self.fig , self.axs = plt.subplots()

    ### treeview
            tv1 = ttk.Treeview(frame3)
            treescrolly = Scrollbar(frame3, orient="vertical", command=tv1.yview) 
            treescrollx = Scrollbar(frame3, orient="horizontal", command=tv1.xview) 
            tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
            treescrolly.pack(side="right",fill=Y)
            treescrollx.pack(side="bottom", fill=X) 
            tv1.pack(side="right",expand=True)
            
            ######
            tv1["column"] = list(data.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column) 

            df_rows = data.to_numpy().tolist() 
            for _ in range(50):
                tv1.insert("", "end", values=df_rows[_])
    ###data-info
            text = Text(self.frame2)
            d = data.describe()
            d=d.convert_dtypes()
            text.insert(END,str(d.iloc[:,:]))
            text.pack(side=LEFT)

            text2 = Text(self.frame2,bg="black",fg="white",font=("Courrier",13))
            text2.insert(END," Le Nombre de lignes: "+str(data.shape[0])+"\n"+" Le Nombre de colonnes: "+str(data.shape[1]))        
            text2.insert(END,"\n__________________________________________________________\n")
            text2.insert(END," Le Nombre des valeurs NaN dans le dataset est: "+ str(data.isnull().sum().sum()))
            text2.insert(END,"\n__________________________________________________________\n")
            text2.insert(END," Les Nan dans chaque attribut : \n\n"+ str(data.isnull().sum()))
            text2.insert(END,"\n__________________________________________________________\n")
            text2.insert(END," Les types des colonnes : \n\n"+ str(data.dtypes))
            text2.pack(side=LEFT)
    ###Bouttons
            basic_graph = Button(frame1,text="basic_graph",font=("Courrier",15),command=self.basic1).pack(fill=X,expand=True,side=LEFT)
            bar_chart = Button(frame1,text="bar_chart",font=("Courrier",15),command=self.bar1).pack(fill=X,expand=True,side=LEFT)
            line_graph = Button(frame1,text="line_graph",font=("Courrier",15),command=self.line1).pack(fill=X,expand=True,side=LEFT)
            histogram = Button(frame1,text="histogram",font=("Courrier",15),command=self.histogram1).pack(fill=X,expand=True,side=LEFT)
            pie_chart = Button(frame1,text="pie_chart",font=("Courrier",15),command=self.pie1).pack(fill=X,expand=True,side=LEFT)
            box_plot = Button(frame1,text="box_plot",font=("Courrier",15),command=self.box1).pack(fill=X,expand=True,side=LEFT)
            grouped_bar_chart = Button(frame1,text="grouped_bar_chart",font=("Courrier",15),command=self.bar2).pack(fill=X,expand=True,side=LEFT)
            quitter = Button(frame1,text="Quitter",font=("Courrier",15),bg="Red",command=lambda:[master.destroy(),root.destroy()]).pack(fill=X,expand=True,side=LEFT)
            saving = Button(frame1,text="Sauvegarder",font=("Courrier",15),bg="Green",command=self.saving).pack(fill=X,expand=True,side=LEFT)

    ###Fonctions pour bouttons
        def basic1(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            val1 = StringVar()
            val2 = StringVar()
            val3 = StringVar()
            val4 = StringVar()
            val5 = StringVar()
            val6 = StringVar()
            
            
            label = Label(root,text="",font=("Courrier",15))
            label.pack(side=RIGHT)
            
            label0 = Label(root,text="Entrez les valeurs séparées par ',' ",font=("Courrier",15)).pack(side=BOTTOM)
            label1 = Label(root,text="axe x :  ",font=("Courrier",15)).pack()
            entry1 = Entry(root,textvariable=val1,font=("Courrier",15)).pack()
            label2 = Label(root,text="axe y : ",font=("Courrier",15)).pack()
            entry2 = Entry(root,textvariable=val2,font=("Courrier",15)).pack()
            label3 = Label(root,text="label : ",font=("Courrier",15)).pack()
            entry3 = Entry(root,textvariable=val3,font=("Courrier",15)).pack()
            label4 = Label(root,text="Titre : ",font=("Courrier",15)).pack()
            entry4 = Entry(root,textvariable=val4,font=("Courrier",15)).pack()
            label5 = Label(root,text="xlabel : ",font=("Courrier",15)).pack()
            entry5 = Entry(root,textvariable=val5,font=("Courrier",15)).pack()
            label6 = Label(root,text="ylabel : ",font=("Courrier",15)).pack()
            entry6 = Entry(root,textvariable=val6,font=("Courrier",15)).pack()
            boutton1 = Button(root,text="Ajouter",font=("Courrier",15),command=lambda:[add_line()]).pack(side=BOTTOM)
            boutton2 = Button(root,text="Sauvegarder",font=("Courrier",15),command=lambda:[save_graph(),root.withdraw()]).pack(side=BOTTOM)
            
            def add_line():
                label['text'] = "Courbe Ajoutée avec succès"
                label['fg'] = "#"+str(random.randrange(100000,999999))
                basic_graph(ax,list(val1.get().split(",")),list(val2.get().split(",")),{'label':val3.get()})
                plt.legend()
                plt.title(val4.get())
                plt.xlabel(val5.get())
                plt.ylabel(val6.get())
                root.update()
                
            def save_graph():
                path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
                flag=True
                i=0
                while flag:
                    try:
                        i+=1
                        open(path2+'/personnaliser_'+val4.get()+str(i)+'.pdf','r')
                        print("Done")
                    except:
                        flag=False
                pdf = PdfPages(path2+'/personnaliser_'+val4.get()+str(i)+'.pdf')
                pdf.savefig( fig )
                pdf.close()
                
                
            
        def bar1(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            val = StringVar()
            val1 = StringVar()
            val2 = StringVar()
            val3 = StringVar()
            
            label1 = Label(root,text="Veillez choisir la variable :  ",font=("Courrier",15)).pack(padx=40,pady=10)
            combo = ttk.Combobox(root, width = 40, textvariable = val)
            combo.pack(padx=40,pady=10)
            combo['values']= tuple(self.all_data.columns.values)
            label2 = Label(root,text="Donnez un titre au graphe : ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry1 = Entry(root,textvariable=val1,font=("Courrier",15))
            entry1.pack(padx=40,pady=10)
            
            boutton2 = Button(root,text="Sauvegarder",font=("Courrier",15),command=lambda:[save_graph(),root.withdraw()]).pack(side=BOTTOM)
            pourcentage = Radiobutton(root, text="en pourcentage",font=("Courrier",10), variable=val2, value="%").pack(padx=40,pady=10)
            pourcentage_0 = Radiobutton(root, text="sans pourcentage",font=("Courrier",10), variable=val3, value="all").pack(padx=40,pady=10)
            
            def save_graph():
                if val2.get() == "%":
                    ax.bar(self.all_data[val.get()].value_counts().index.tolist(),[x/sum(self.all_data[val.get()].value_counts().values.tolist())*100 for x in self.all_data[val.get()].value_counts().values.tolist()],\
                           label=self.all_data[val.get()].value_counts().index.tolist())
                else:
                    ax.bar(self.all_data[val.get()].value_counts().index.tolist(),self.all_data[val.get()].value_counts().values.tolist(),label=self.all_data[val.get()].value_counts().index.tolist())

                plt.title(val1.get())
                path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
                flag=True
                i=0
                while flag:
                    try:
                        i+=1
                        open(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf','r')
                        print("Done")
                    except:
                        flag=False
                pdf = PdfPages(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf')
                pdf.savefig( fig )
                pdf.close()
        
        def line1(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            
            val = StringVar()
            val0 = StringVar()
            val1 = StringVar()
            val2 = StringVar()
            
            label1 = Label(root,text="Veillez choisir la variable pour axe X:  ",font=("Courrier",15)).pack(padx=40,pady=10)
            combo = ttk.Combobox(root, width = 40, textvariable = val)
            combo.pack(padx=40,pady=10)
            combo['values']= tuple(self.all_data.columns.values)
            label2 = Label(root,text="Veillez choisir la variable pour axe Y:  ",font=("Courrier",15)).pack(padx=40,pady=10)
            combo1 = ttk.Combobox(root, width = 40, textvariable = val0)
            combo1.pack(padx=40,pady=10)
            combo['values']= tuple(self.all_data.columns.values)
            label3 = Label(root,text="Donnez un titre au graphe : ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry1 = Entry(root,textvariable=val1,font=("Courrier",15))
            entry1.pack(padx=40,pady=10)
            label4 = Label(root,text="Donnez un label : ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry2 = Entry(root,textvariable=val2,font=("Courrier",15))
            entry2.pack(padx=40,pady=10)
            
            
            boutton2 = Button(root,text="Sauvegarder",font=("Courrier",15),command=lambda:[save_graph(),root.withdraw()]).pack(side=BOTTOM)
        
            
            def save_graph():
                
                line_graph(ax,self.all_data[val.get()].value_counts().values.tolist(),self.all_data[val0.get()].value_counts().values.tolist(),{'label':val2.get()})

                plt.title(val1.get())
                path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
                flag=True
                i=0
                while flag:
                    try:
                        i+=1
                        open(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf','r')
                        print("Done")
                    except:
                        flag=False
                pdf = PdfPages(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf')
                pdf.savefig( fig )
                pdf.close()
            
        def histogram1(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            val = StringVar()
            val1 = StringVar()
            val2 = StringVar()
            
            label1 = Label(root,text="Veillez choisir la variable :  ",font=("Courrier",15)).pack(padx=40,pady=10)
            combo = ttk.Combobox(root, width = 40, textvariable = val)
            combo.pack(padx=40,pady=10)
            combo['values']= tuple(self.all_data.columns.values)
            label2 = Label(root,text="Veillez donner l'interval :  ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry0 = Entry(root,textvariable=val1,font=("Courrier",15))
            entry0.pack(padx=40,pady=10)
            label2 = Label(root,text="Donnez un titre au graphe : ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry1 = Entry(root,textvariable=val2,font=("Courrier",15))
            entry1.pack(padx=40,pady=10)
           
            def save_graph():

                histogram(ax,self.all_data[val.get()].value_counts().values.tolist(),list[val1.get()],{'label':val2.get()})

                plt.title(val1.get())
                path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
                flag=True
                i=0
                while flag:
                    try:
                        i+=1
                        open(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf','r')
                        print("Done")
                    except:
                        flag=False
                pdf = PdfPages(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf')
                pdf.savefig( fig )
                pdf.close()
            
        def pie1(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            val = StringVar()
            val1 = StringVar()
            val2 = StringVar()
            val3 = StringVar()
            
            label1 = Label(root,text="Veillez choisir la variable :  ",font=("Courrier",15)).pack(padx=40,pady=10)
            combo = ttk.Combobox(root, width = 40, textvariable = val)
            combo.pack(padx=40,pady=10)
            combo['values']= tuple(self.all_data.columns.values)
            label2 = Label(root,text="Donnez un titre au graphe : ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry1 = Entry(root,textvariable=val1,font=("Courrier",15))
            entry1.pack(padx=40,pady=10)
            
            boutton2 = Button(root,text="Sauvegarder",font=("Courrier",15),command=lambda:[save_graph(),root.withdraw()]).pack(side=BOTTOM)
            pourcentage = Radiobutton(root, text="en pourcentage",font=("Courrier",10), variable=val2, value="%").pack(padx=40,pady=10)
            pourcentage_0 = Radiobutton(root, text="sans pourcentage",font=("Courrier",10), variable=val3, value="all").pack(padx=40,pady=10)
            
            def save_graph():
                if val2.get() == "%":
                    ax.pie(self.all_data[val.get()].value_counts().index.tolist(),[x/sum(self.all_data[val.get()].value_counts().values.tolist())*100 for x in self.all_data[val.get()].value_counts().values.tolist()])
                else:
                    ax.bar(self.all_data[val.get()].value_counts().index.tolist(),self.all_data[val.get()].value_counts().values.tolist(),label=self.all_data[val.get()].value_counts().index.tolist())

                plt.title(val1.get())
                path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
                flag=True
                i=0
                while flag:
                    try:
                        i+=1
                        open(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf','r')
                        print("Done")
                    except:
                        flag=False
                pdf = PdfPages(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf')
                pdf.savefig( fig )
                pdf.close()
            
            
        def box1(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            val = StringVar()
            val1 = StringVar()
            
            label1 = Label(root,text="Veillez choisir la variable :  ",font=("Courrier",15)).pack(padx=40,pady=10)
            combo = ttk.Combobox(root, width = 40, textvariable = val)
            combo.pack(padx=40,pady=10)
            combo['values']= tuple(self.all_data.columns.values)
            label2 = Label(root,text="Donnez un titre au graphe : ",font=("Courrier",15)).pack(padx=40,pady=10)
            entry1 = Entry(root,textvariable=val1,font=("Courrier",15))
            entry1.pack(padx=40,pady=10)
            
            def save_graph():
                
                box_plot(ax,self.all_data[val.get()].value_counts().values.tolist(),val.get())

                plt.title(val1.get())
                path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
                flag=True
                i=0
                while flag:
                    try:
                        i+=1
                        open(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf','r')
                        print("Done")
                    except:
                        flag=False
                pdf = PdfPages(path2+'/personnaliser_'+val1.get()+str(i)+'.pdf')
                pdf.savefig( fig )
                pdf.close()
            
        def bar2(self):
            root.deiconify()
            for item in root.winfo_children():
                item.destroy()
            fig,ax = plt.subplots()
            val = StringVar()
            
        def saving(self):
            pass
## Fonction pour loading
def loading_win():
    master = Tk()
    master.title("Loading")
    master.config(background="black")
    label = Label(master,text="Loading...",font=("Cambria",15,"bold")).pack()
    master.iconbitmap("hcp_esi_img.ico")
    master.update()

    return master
#Fonction pour convertir
def Spss_excel():
    # SPSS to Excel
    path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier à convertir",filetypes=(("Fichier spss","*.sav"),("Tous les fichiers","*.*")))
    data = read_data(path)
    path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
    flag = True
    i=0
    while flag:
        try:
            i+=1
            open(path2+"/converted"+str(i)+".xlsx",'r')
        except:
            flag = False
    data.to_excel(path2+"/converted"+str(i)+".xlsx")
    messagebox.showinfo("Success","Opération terminée",parent=root)

    

def Spss_csv():
    # SPSS to Csv
    path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier à convertir",filetypes=(("Fichier excel","*.xlsx"),("Fichier excel","*.xls"),("Tous les fichiers","*.*")))
    data = read_data(path)
    path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
    flag = True
    i=0
    while flag:
        try:
            i+=1
            open(path2+"/converted"+str(i)+".csv",'r')
        except:
            flag = False
    data.to_csv(path2+"/converted"+str(i)+".csv")
    messagebox.showinfo("Success","Opération terminée",parent=root)


def Excel_csv():
    # Excel to Csv
    path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier à convertir",filetypes=(("Fichier excel","*.xlsx"),("Fichier excel","*.xls"),("Tous les fichiers","*.*")))
    data = read_data(path)
    path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
    flag = True
    i=0
    while flag:
        try:
            i+=1
            open(path2+"/converted"+str(i)+".csv",'r')
        except:
            flag = False
    data.to_csv(path2+"/converted"+str(i)+".csv")
    messagebox.showinfo("Success","Opération terminée",parent=root)


def Csv_excel():
    # Csv to Excel
    path=filedialog.askopenfilename(initialdir="/",title="Selectionnez le fichier à convertir",filetypes=(("Fichier csv","*.csv"),("Tous les fichiers","*.*")))
    data = read_data(path)
    path2 = filedialog.askdirectory (title = "Sélectionnez un répertoire de destination ...")
    flag = True
    i=0
    while flag:
        try:
            i+=1
            open(path2+"/converted"+str(i)+".xlsx",'r')
        except:
            flag = False
    data.to_excel(path2+"/converted"+str(i)+".xlsx")
    messagebox.showinfo("Success","Opération terminée",parent=root)
#Main

root = Tk()
login = Login(root)
root.mainloop()
 