from django.shortcuts import render
from alumno.alumno import alumno

def pintarAlumno(request):
    a1 = alumno("Axel","León",20,"20233TN175")

    # ¿Me está llegando info de un form?
    if request.method == "POST":
        #Tratar esa info
        nombre = request.POST.get("nombre")
        nombre = nombre.upper()

        return render (
            request,
            "alumno/informacion.html",
            {"seEnvio":True, "nombre": nombre}
        )

    ##Render
    return render (
        request, 
        "alumno/informacion.html",
        {
            "alumno1":a1, 
            "alumno2":alumno("Daniel", "Flores", 15, "2312456")    
        }
        )