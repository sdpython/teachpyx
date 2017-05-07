# -*- coding: utf-8 -*-
"""module contenant une boîte de dialogue permettant 
de sélectionner un fichier ou un répertoire,
il utilise l'interface Tkinter"""
import tkinter
import os.path
import os

class FileSelection(object) :
    """classe permettant de sélectionner un fichier 
    ou un répertoire à travers une boîte de dialogue"""
    
    def __init__(self, parent, titre = "Sélection de fichier", \
                    chemin = None, file = True, exist= True) :
        """
        initialise la classe
        
        @param      parent          parent
        @param      titre           titre de la fenêtre
        @param      chemin          fichier ou répertoire par défaut
        @param      file            True : fichier, False : répertoire
        @param      exist           True : le répertoire ou le fichier 
                                           sélectionné doit exister"""
        self.parent = parent
        self.titre  = titre
        self.chemin = chemin
        self.file   = file
        self.exist  = exist
        
        if self.chemin is None:
            self.chemin = os.getcwd()
            
    def get_list(self) :
        """retourne la liste des fichiers et des répertoires(2 listes), 
        répertoires seulement et [] si self.file == False"""
        if os.path.isdir(self.chemin):
            listf    = os.listdir(self.chemin)
        else : 
            ch, fi   = os.path.split(self.chemin)
            listf    = os.listdir(ch)
        
        lifile  = []
        lidir   = []
        for l in listf:
            if os.path.isdir(self.chemin + "\\" + l) : 
                lidir.append(l)
            elif self.file: 
                lifile.append(l)
                
        lidir.sort()
        lifile.sort()
        return lidir, lifile
        
    def run(self) :
        """lance la boîte de dialogue et retourne la chaîne sélectionnée"""
        if self.parent is None:
            top         = tkinter.Toplevel()
            top.wm_title(self.titre)
        else:
            top = self.parent
        self.resultat = False

        fli = tkinter.Frame(top)
        scrollbar = tkinter.Scrollbar(fli)
        li = tkinter.Listbox(fli, width = 120, height = 15, \
                              yscrollcommand = scrollbar.set)
        scrollbar.config(command = li.yview)
        ch      = tkinter.Entry(top, width = 120)
        f       = tkinter.Frame(top)
        prec    = tkinter.Button(f, text = "Précédent")
        suiv    = tkinter.Button(f, text = "Entre")
        annul   = tkinter.Button(f, text = "Annuler")        
        ok      = tkinter.Button(f, text = "Ok")        
        
        prec.grid(column = 0, row = 0)
        suiv.grid(column = 1, row = 0)
        annul.grid(column = 3, row = 0)
        ok.grid(column = 4, row = 0)
        li.pack(side = tkinter.LEFT)
        scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)
        fli.pack()
        ch.pack()
        f.pack()

        def update_chemin() :
            """mise à jour du chemin dans la boîte de dialogue"""
            s = ch.get()
            ch.delete(0, len(s))
            ch.insert(0, self.chemin)

        def update_list() :
            """mise à jour de la liste des fichiers et répertoires 
            à partir de la chaîne dans la boîte de dialogue"""
            self.chemin     = ch.get()
            lidir, lifile   = self.get_list()
            li.delete(0, tkinter.END)
            if len(lidir) > 0 : 
                for l in lidir: 
                    li.insert(tkinter.END, "+ "+ l)
            if len(lifile) > 0: 
                for l in lifile: 
                    li.insert(tkinter.END, "  "+ l)
                    
        def precedent() :
            """passe au répertoire précédent"""
            if os.path.isdir(self.chemin) :
                ch, last    = os.path.split(self.chemin)
                self.chemin = ch
            else :
                ch, last    = os.path.split(self.chemin)
                ch, last    = os.path.split(ch)
                self.chemin = ch
            update_chemin()
            update_list()
        
        def suivant() :
            """rentre dans un répertoire"""
            sel = ch.get()
            if os.path.isdir(sel) :
                self.chemin = sel
                update_chemin()
                update_list()
            
        def update_sel() :
            """mise à jour de la chaîne de caractères 
            dans la boîte de dialogue à partir de la ligne
            sélectionnée dans la liste"""
            li.after(200, update_sel)
            sel = li.curselection()
            if len(sel) == 1 :
                t = li.get(sel [0])
                c = self.chemin + "\\" +  t [2:len(t)]
                s = ch.get()
                ch.delete(0, len(s))
                ch.insert(0, c)
                
        def annuler() :
            """annule la recherche"""
            self.resultat = False
            top.destroy()
            top.quit()
        
        def accepter() :
            """accepte le résultat"""
            self.resultat    = True
            self.chemin = ch.get()
            top.destroy()
            top.quit()
            
        prec.config(command = precedent)
        suiv.config(command = suivant)
        annul.config(command = annuler)
        ok.config(command = accepter)
                
        update_chemin()
        update_list()
        update_sel()
        ch.focus_set()
        
        if self.parent is None:
            top.mainloop()        
            
            
if __name__ == "__main__" :
    
    def run(root) :
        r = FileSelection(root, "sélection d'un fichier", "c:\\")
        s = r.run()
        return r
        
    root = tkinter.Tk()
    win = run(root)
    root.mainloop()
    print("fichier sélectionné ", win.chemin)
