from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Empresa, Insumo, Turno, Colaborador
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.lib.units import cm
#
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
#

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "Web Aseo Integral"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"

@method_decorator(staff_member_required, name='dispatch')
def formularioEmpresa(request):
    resp = False
    if request.POST:
        ru = request.POST.get('rutEmpresa', '')
        di = request.POST.get('direccion', '')
        ra = request.POST.get('razonSocial', '')
        co = request.POST.get('correo', '')
        te = request.POST.get('telefono', '')
        emp = Empresa(
            rutEmpresa=ru,
            direccion=di,
            razonSocial=ra,
            correo=co,
            telefono=te
        )
        emp.save()
        resp = True
    return render(request, 'core/formularioempresa.html', {'respuesta': resp})

@method_decorator(staff_member_required, name='dispatch')
def actualizarEmpresa(request):
    em = Empresa.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            rut = request.POST.get("rutEmpresa", "")
            emp = Empresa.objects.get(rutEmpresa=rut)
            mensaje = False
            return render(request, 'core/actualizarempresa.html', {'empresas': em, 'emp': emp, 'mensaje': mensaje})
        if accion == "Modificar":
            rut = request.POST.get("rutEmpresa", "")
            emp = Empresa.objects.get(rutEmpresa=rut)
            direccion = request.POST.get("direccion", "")
            razonSocial = request.POST.get("razonSocial", "")
            correo = request.POST.get("correo", "")
            telefono = request.POST.get("telefono", "")
            emp.direccion = direccion
            emp.razonSocial = razonSocial
            emp.correo = correo
            emp.telefono = telefono
            emp.save()
            mensaje = True
            return render(request, 'core/actualizarempresa.html', {'empresas': em, 'mensaje': mensaje})
    return render(request, 'core/actualizarempresa.html', {'empresas': em})

@method_decorator(staff_member_required, name='dispatch')
def eliminarEmpresa(request):
    em = Empresa.objects.all()
    resp = False
    if request.POST:
        rut = request.POST.get('rutEmpresa', "")
        emp = Empresa.objects.get(rutEmpresa=rut)
        emp.delete()
        resp = True
    return render(request, 'core/eliminarempresa.html', {'empresas': em, 'respuesta': resp})

@method_decorator(staff_member_required, name='dispatch')
def listarEmpresa(request):
    em = Empresa.objects.all()
    return render(request, 'core/listarempresa.html', {'empresas': em})

@method_decorator(staff_member_required, name='dispatch')
def formularioColaborador(request):
    resp = False
    if request.POST:
        ru = request.POST.get('rut', '')
        no = request.POST.get('nombreCompleto', '')
        se = request.POST.get('sexo', '')
        fe = request.POST.get('fechaNacimiento', '')
        di = request.POST.get('direccion', '')
        te = request.POST.get('telefono', '')
        col = Colaborador(
            rut=ru,
            nombreCompleto=no,
            sexo=se,
            fechaNacimiento=fe,
            direccion=di,
            telefono=te
        )
        col.save()
        resp = True
    return render(request, 'core/formulariocolaborador.html', {'respuesta': resp})

@method_decorator(staff_member_required, name='dispatch')
def actualizarColaborador(request):
    co = Colaborador.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            rut = request.POST.get("rut", "")
            col = Colaborador.objects.get(rut=rut)
            mensaje = False
            return render(request, 'core/actualizarcolaborador.html', {'colaboradores': co, 'col': col, 'mensaje': mensaje})
        if accion == "Modificar":
            rut = request.POST.get("rut", "")
            col = Colaborador.objects.get(rut=rut)
            nombreCompleto = request.POST.get("nombreCompleto", "")
            sexo = request.POST.get("sexo", "")
            fechaNacimiento = request.POST.get("fechaNacimiento", "")
            direccion = request.POST.get("direccion", "")
            telefono = request.POST.get("telefono", "")
            col.nombreCompleto = nombreCompleto
            col.sexo = sexo
            col.fechaNacimiento = fechaNacimiento
            col.direccion = direccion
            col.telefono = telefono
            col.save()
            mensaje = True
            return render(request, 'core/actualizarcolaborador.html', {'colaboradores': co, 'mensaje': mensaje})
    return render(request, 'core/actualizarcolaborador.html', {'colaboradores': co})

@method_decorator(staff_member_required, name='dispatch')
def eliminarColaborador(request):
    co = Colaborador.objects.all()
    resp = False
    if request.POST:
        rut = request.POST.get('rut', "")
        col = Colaborador.objects.get(rut=rut)
        col.delete()
        resp = True
    return render(request, 'core/eliminarcolaborador.html', {'colaboradores': co, 'respuesta': resp})

@method_decorator(staff_member_required, name='dispatch')
def listarColaborador(request):
    co = Colaborador.objects.all()
    return render(request, 'core/listarcolaborador.html', {'colaboradores': co})

@method_decorator(staff_member_required, name='dispatch')
def formularioTurno(request):
    resp = False
    if request.POST:
        la=request.POST["txtLat"]
        lo=request.POST["txtLon"]
        fecha = request.POST["fecha"]
        rut=request.POST["rut"]
        registro=request.POST["cbRegistro"]
        obj_col = Colaborador.objects.get(rut=rut)
        ub = Turno(
            latitud=la,
            longitud=lo,
            fecha=fecha,
            registro=registro,
            rut=obj_col
        )
        ub.save()
        resp=True
    return render(request, 'core/formularioturno.html',{'respuesta':resp})

@method_decorator(staff_member_required, name='dispatch')
def formularioInsumo(request):
    emp = Empresa.objects.all()
    resp = False
    if request.POST:
        idProducto = request.POST.get("idProducto", "")
        nombre = request.POST.get("nombre", "")
        stock = request.POST.get("stock","")
        rutEmp = request.POST.get("rutEmpresa","")
        obj_empresa = Empresa.objects.get(rutEmpresa=rutEmp)
        ins = Insumo(
            idProducto=idProducto,
            nombre=nombre,
            stock=stock,
            rutEmpresa=obj_empresa
        )
        ins.save()
        resp = True
    return render(request, 'core/formularioinsumo.html', {'respuesta': resp, 'empresa': emp})

@method_decorator(staff_member_required, name='dispatch')
def listarInsumo(request):
    ins = Insumo.objects.all()
    return render(request, 'core/listarinsumo.html', {'insumos': ins})

@method_decorator(staff_member_required, name='dispatch')
def eliminarInsumo(request):
    ins = Insumo.objects.all()
    resp = False
    if request.POST:
        idp = request.POST.get("idProducto", "")
        insu = Insumo.objects.get(idProducto=idp)
        insu.delete()
        resp = True
    return render(request, 'core/eliminarinsumo.html', {'insumos': ins, 'respuesta': resp})

@method_decorator(staff_member_required, name='dispatch')
def actualizarInsumo(request):
    emp = Empresa.objects.all()
    insu = Insumo.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            idp = request.POST.get("idProducto", "")
            ins = Insumo.objects.get(idProducto=idp)
            mensaje = False
            return render(request, 'core/actualizarinsumo.html', {'insumos':insu,'empresas':emp, 'ins': ins, 'mensaje': mensaje})
        if accion == "Modificar":
            idp = request.POST.get("idProducto", "")
            ins = Insumo.objects.get(idProducto=idp)

            idProducto = request.POST.get("idProducto", "")
            nombre = request.POST.get("nombre", "")
            stock = request.POST.get("stock","")
            rutEmp = request.POST.get("rutEmpresa","")
            obj_empresa = Empresa.objects.get(rutEmpresa=rutEmp)
            ins.idProducto=idProducto
            ins.nombre=nombre
            ins.stock=stock
            ins.rutEmpresa=obj_empresa
            ins.save()
            mensaje = True
            return render(request, 'core/actualizarinsumo.html', {'mensaje': mensaje, 'empresa': emp})
    return render(request, 'core/actualizarinsumo.html', {'mensaje': mensaje,'insumos':insu, 'empresa': emp})

@method_decorator(staff_member_required, name='dispatch')
class ReportePersonasPDF(View):

    def cabecera(self, pdf):
        # Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo_django.png'
        # Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120,
                      90, preserveAspectRatio=True)

    def tabla(self, pdf, y):
        # Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Rut', 'Nombre Completo', 'Sexo',
                       'Fecha nacimiento', 'Direccion', 'Telefono')
        # Creamos una lista de tuplas que van a contener a las personas
        detalles = [(Colaborador.rut, Colaborador.nombreCompleto, Colaborador.sexo,
                     Colaborador.fechaNacimiento, Colaborador.direccion, Colaborador.telefono) for Colaborador in Colaborador.objects.all()]
        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles,
                              colWidths=[2.2 * cm, 4.5 * cm, 1.6 * cm, 2.9 * cm, 5 * cm, 2.2 * cm])
        # Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 40, y)

    def get(self, request, *args, **kwargs):

        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        # Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        # Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        # Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(240, 790, u"ASEO INTEGRAL")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE COLABORADORES")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(
            40, 720, "Detale de colaboradores registrados actualmente.")
        y = 600
        self.tabla(pdf, y)
        # Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
