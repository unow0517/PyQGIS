from PyQt5.QtCore import *
from PyQt5.QtGui import *
import QMetaTiles
import random
def randomColor(mix=(255,255,255)):
    red = random.randrange(0,256)
    green = random.randrange(0,256)
    blue = random.randrange(0,256)
    r,g,b = mix
    red = (red + r)/2
    green = (green+g)/2
    blue = (blue + b)/2
    return (red,green,blue)
def done():
    print ("FINISHED!!")

shp = 'C:/Users/unow1/Desktop/Programming/\
PyQGIS/MapData/DEU_adm/DEU_adm1.shp'
dir = 'C:/Users/unow1/Desktop/Programming/\
PyQGIS/tileCache'


###QgsVectorLayer(path, baseName, providerLibrary)##
layer = QgsVectorLayer(shp, "YunHo_New_Map", 'ogr')
field = 'NAME_1'
features = layer.getFeatures()
categories = []
for feature in features:
    state = feature[field]
    ##ClassQgsSymbol.defaultSymbol = 
    ##return new default symbol for specified geometry type
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    r,g,b = randomColor()
    ##QColor from QtGUI, last Number = opacity
    sym.setColor(QColor(r,g,b,200))
    ##QgsRendererCategory(value,QgsSymbol,Label)
    category = QgsRendererCategory(state, sym, state)
    categories.append(category)

renderer = QgsCategorizedSymbolRenderer(field, categories)
layer.setRenderer(renderer)

QgsProject.instance().addMapLayer(layer)


##Labeling##

##A pal object will contains layers and 
##global information such as which search method 
##will be used, the map resolution (dpi) ....
layer_settings = QgsPalLayerSettings()

text_format = QgsTextFormat()
text_format.setSize(12)

buffer_settings = QgsTextBufferSettings()
buffer_settings.setEnabled(True)
buffer_settings.setSize(1)
buffer_settings.setColor(QColor("white"))

text_format.setBuffer(buffer_settings)
layer_settings.setFormat(text_format)

layer_settings.fieldName = "NAME_1"
layer_settings.placement = 1

layer_settings.enabled = True

layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
layer.setLabelsEnabled(True)
layer.setLabeling(layer_settings)
layer.triggerRepaint()
##Labeling end##






    