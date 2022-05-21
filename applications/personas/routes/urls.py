from django.contrib import admin
from django.urls import path
from ..views import (
    ListAllEmpleados,
    ListEmpleadosByArea,
    ListEmpleadosByJob,
    ListEmpleadoByKeyWord,
    ListHabilidadesEmpleados,
    EmpleadoDetailView,
    CreateEmpleado,
    SuccesView,
    EmpleadoUpdate,
    DeleteEmpleado,
    InicioView,
    ListAllEmpleadosAdmin
)
app_name="empleados_app"
urlpatterns = [
    path('', InicioView.as_view()),
    path(
        'empleados/',
        ListAllEmpleados.as_view(),
        name="empleados_all" ),
    #párametros en una url
    path(
        'empleados-by-area/<departamento>/',
        ListEmpleadosByArea.as_view(),
        name='empleados_by_area'
        ),
    path(
        'empleados-admin/',
        ListAllEmpleadosAdmin.as_view(),
        name='empleados_admin'
        ),
    path('empleados-by-job/<job>/', ListEmpleadosByJob.as_view()),
    path('empleados-by-word/', ListEmpleadoByKeyWord.as_view()),
    path('empleados-habilidades/', ListHabilidadesEmpleados.as_view()),
    path(
        'empleados-detalle/<pk>/', 
        EmpleadoDetailView.as_view(),
        name='empleado-detail'
        ),
    path(
        'create-empleados/', 
        CreateEmpleado.as_view(),
        name='add_empleado'
        ),
    path('success/',SuccesView.as_view(),name='empleado_created'),
    path(
        'empleados-update/<pk>/',
        EmpleadoUpdate.as_view(),
        name='empleado-edit'
        ),
    path(
        'empleados-delete/<pk>/',
        DeleteEmpleado.as_view(),
        name='empleado-delete'
        ),

]
