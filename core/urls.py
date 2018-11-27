from django.urls import path
from .views import HomePageView, SamplePageView
from .views import formularioEmpresa, actualizarEmpresa, eliminarEmpresa, listarEmpresa, formularioColaborador, actualizarColaborador, eliminarColaborador, listarColaborador, ReportePersonasPDF, formularioInsumo, listarInsumo, eliminarInsumo, actualizarInsumo, formularioTurno


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('formulario_empresa', formularioEmpresa, name='formularioEmpresa'),
    path('actualizar_empresa', actualizarEmpresa, name='actualizarEmpresa'),
    path('eliminar_empresa', eliminarEmpresa, name='eliminarEmpresa'),
    path('listar_empresa', listarEmpresa, name='listarEmpresa'),
    path('formularioinsumo',formularioInsumo, name="formin"),
    path('listarinsumo',listarInsumo, name="listin"),
    path('eliminarinsumo',eliminarInsumo,name="elimin"),
    path('actualizarinsumo',actualizarInsumo,name="actuain"),
    path('formularioturno',formularioTurno,name="formtu"),
    path('formulario_colaborador', formularioColaborador,
         name='formularioColaborador'),
    path('actualizar_colaborador', actualizarColaborador,
         name='actualizarColaborador'),
    path('eliminar_colaborador', eliminarColaborador, name='eliminarColaborador'),
    path('listar_colaborador', listarColaborador, name='listarColaborador'),
    path('pdf_colaboradores', ReportePersonasPDF.as_view(),
         name="pdf_colaboradores"),
    path('sample/', SamplePageView.as_view(), name="sample"),

]
