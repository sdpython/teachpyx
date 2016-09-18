# coding: latin-1

import sys
import os

default_path     = r"C:\Program Files\gp423win32\gnuplot\bin\pgnuplot.exe"
default_temp_dir = "tempgnuplot"
imagenumber      = 0

def execute_script_gnuplot (scr) :
    global default_temp_dir
    global imagenumber
    global default_path

    if not os.path.exists (default_temp_dir) : os.mkdir (default_temp_dir)

    # avant
    scr          = "set term png\n" + scr
    image        = default_temp_dir + ("/image_%05d.png" % imagenumber)
    imagenumber += 1
    scr          = "set out \"" + image + "\"\n" + scr

    # après
    scr += "show out\n"
    scr += "exit\n"

    name = default_temp_dir + "/gnuscript.txt"
    f    = open (name, "w")
    f.write (scr)
    f.close ()

    line = default_path + " " + name
    os.system (line)

    return image

def build_script_gnuplot (series, seriesname, title = None, \
                     xlabel = None, ylabel = None, histo = False) :
    global default_temp_dir
    global default_path

    if not os.path.exists (default_temp_dir) : os.mkdir (default_temp_dir)
    scr = ""

    if xlabel != None : scr += "set xlabel \"" + xlabel + "\"\n"
    if ylabel != None : scr += "set ylabel \"" + ylabel + "\"\n"
    if title  != None : scr += "set title \"" + title + "\"\n"

    scr += "set grid\n"
    if histo : scr += "set style data histograms\n"
    else : scr += "set style data lines\n"
    scr += "plot "

    id = 0
    for s,lab in zip (series, seriesname) :
        name = default_temp_dir + "/series%d.txt" % (id)
        id  += 1
        f    = open (name, "w")
        for l in s :
            if histo : f.write ("%f\n" % (l [1]))
            else : f.write ("%f\t%f\n" % (l [0], l [1]))
        f.close ()
        scr += "\"" + name + "\" title \"" + lab + "\", "
    scr = scr [:len (scr)-2]
    scr += "\n"

    return execute_script_gnuplot (scr)


if __name__ == "__main__" :
    print "chemin pour gnuplot ", default_path

    series = [ [], [] ]
    for i in range (0, 100) :
        x = float (i) / 100
        y = x ** 0.5
        z = 1.0 - y
        series [0].append ( (x,y) )
        series [1].append ( (x,z) )

    image = build_script_gnuplot (series, ["serie 1", "serie 2"], \
                        xlabel="abscisses", ylabel="ordonnées", histo = False)
    print "image ", image
    image = build_script_gnuplot (series, ["serie 1", "serie 2"], \
                        xlabel="abscisses", ylabel="ordonnées", histo = True)
    print "image ", image
