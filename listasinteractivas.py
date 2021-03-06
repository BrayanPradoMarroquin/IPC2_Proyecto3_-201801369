import xml.etree.ElementTree as ET
class Eventoss:
    def __init__(self, fecha, cantidad, usuarios, afectados, errores):
        self.fecha=fecha
        self.cantidad = cantidad
        self.usuarios = usuarios
        self.afectados = afectados
        self.errores = errores

class Usuarioss:
    def __init__(self, user, cant):
        self.user = user
        self.cant = cant

listaux1=[]
listaux2=[]
fechas=[]
usuarios=[]
Afectados=[]
errores=[]
usuarioxfech=None

#iterara las listas en base a la peticiones
def usuarioxfecha(fecha):
    global fechas, usuarioxfech
    usuarioxfech=None
    for Fecha in fechas:
        if Fecha.fecha==fecha:
            usuarioxfech=Fecha.usuarios
    if usuarioxfech!=None:
        return usuarioxfech
    else:
        return "No existe dicha fecha"

#iterara las listas en base a la peticion de fechas
def errorxfecha(fecha):
    global fechas, usuarioxfech
    usuarioxfech=[]
    for Fecha in fechas:
        if Fecha.fecha==fecha:
            usuarioxfech=Fecha.errores
    if usuarioxfech!=None:
        return usuarioxfech
    else:
        return "No existe dicha fecha"

#realiza la lista de eventos en base a las fechas
def listar(listaEventos):
    global listaux1, listaux2, fechas, usuarios, Afectados, errores
    for fe in listaEventos:
        if fe.Fecha not in listaux1:
            listaux1.append(fe.Fecha)
    for f in listaux1:
        cont=0
        for l in listaEventos:
            if l.Fecha==f:
                cont+=1
                usuarios.append(l.Usuario)
                Afectados = Afectados + l.Reportados
                errores.append(l.Error)
        fechas.append(Eventoss(f,cont, usuarios, Afectados, errores))
        usuarios=[]
        Afectados=[]
        errores=[]
    listaux1=[]

    for dd in fechas:
        usuariofecha = dd.usuarios
        for usuario in usuariofecha:
            if usuario not in listaux2:
                listaux2.append(usuario)
        for f in listaux2:
            cont=0
            for l in usuariofecha:
                if l==f:
                    cont+=1
            usuarios.append(Usuarioss(f, cont))
        dd.usuarios = usuarios
        listaux2=[]
        usuarios=[]

    for dd in fechas:
        usuariofecha = dd.afectados
        for usuario in usuariofecha:
            if usuario not in listaux2:
                listaux2.append(usuario)
        for f in listaux2:
            cont=0
            for l in usuariofecha:
                if l==f:
                    cont+=1
            usuarios.append(Usuarioss(f, cont))
        dd.afectados = usuarios
        listaux2=[]
        usuarios=[]

    for dd in fechas:
        usuariofecha = dd.errores
        for usuario in usuariofecha:
            if usuario not in listaux2:
                listaux2.append(usuario)
        for f in listaux2:
            cont=0
            for l in usuariofecha:
                if l==f:
                    cont+=1
            usuarios.append(Usuarioss(f, cont))
        dd.errores = usuarios
        listaux2=[]
        usuarios=[]

#genera el archivo de estaditica en formato xml
def generarxml():
    global fechas
    ESTADISTICAS = ET.Element('ESTADISTICAS')
    for fecha in fechas:
        ESTADISTICA = ET.SubElement(ESTADISTICAS, 'ESTADISTICA')
        FECHA = ET.SubElement(ESTADISTICA, 'FECHA')
        FECHA.text = fecha.fecha
        CANTIDAD = ET.SubElement(ESTADISTICA, 'CANTIDAD_MENSAJES')
        CANTIDAD.text = str(fecha.cantidad)
        REPORTADO = ET.SubElement(ESTADISTICA, 'REPORTADO_POR')
        for user in fecha.usuarios:
            USUARIOS = ET.SubElement(REPORTADO, 'USUARIO')
            EMAIL = ET.SubElement(USUARIOS, 'EMAIL')
            EMAIL.text = user.user
            CANTIDADUSUARIO = ET.SubElement(USUARIOS, 'CANTIDAD_MENSAJES')
            CANTIDADUSUARIO.text = str(user.cant)
        AFECTADOS = ET.SubElement(ESTADISTICA, 'AFECTADOS')
        for afec in fecha.afectados:
            AFECTADO = ET.SubElement(AFECTADOS, 'AFECTADO')
            AFECTADO.text = afec.user
        ERRORES = ET.SubElement(ESTADISTICA, 'ERRORES')
        for error in fecha.errores:
            ERROR = ET.SubElement(ERRORES, 'ERROR')
            CODIGO = ET.SubElement(ERROR, 'CODIGO')
            CODIGO.text = error.user
            CANTIDADERROR = ET.SubElement(ERROR, 'CANTIDAD_MENSAJES')
            CANTIDADERROR.text = str(error.cant)
    mydata = ET.tostring(ESTADISTICAS)
    myfile = open('estadistica.xml', "w")
    myfile.write(str(mydata))
    myfile.close()
    print('Archivo generado con exito')