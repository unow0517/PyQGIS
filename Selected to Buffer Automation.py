layer = iface.activeLayer()
selected = layer.selectedFeatures()
outfile = 'C:/Users/unow1/Desktop/Programming/PyQGIS/buffer.shp'
fields=layer.fields()
bufDist = 5

writer = QgsVectorFileWriter(outfile,'UTF-8',fields,
QgsWkbTypes.Polygon, layer.sourceCrs(),'ESRI shapefile')


for i in selected:
    geom = i.geometry()
    buffer = geom.buffer(bufDist,10)
    i.setGeometry(buffer)
    writer.addFeature(i)

print('done')
iface.addVectorLayer(outfile,'','ogr')
del(writer)
    