<%@page import="com.ipn.mx.modelo.dto.CategoriaDTO"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Actualizar Categoria</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" ></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>
    </head>
    <body class="p-3 mb-2 bg-dark text-white">
        <!-- NAVBAR---------------------------------------------------------------NAVBAR -->
        <div>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="/ProyectoBase3CM18-V2/index.jsp">Proyecto Base V2</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class='nav-item'>
                                <a class='nav-link active' aria-current='page' href='/ProyectoBase3CM18-V2/TablaDeMultiplicar.jsp'>TablaDeMultiplicar</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='/ProyectoBase3CM18-V2/Productos/listaDeProductos.jsp'>Mostrar Productos</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='listaDeCategorias.jsp'>Mostrar Categorias</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='nuevaCategoriaForm.jsp'>Crear Categoria</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='/ProyectoBase3CM18-V2/Productos/nuevoProductoForm.jsp'>Crear Producto</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
        <!-- NAVBAR---------------------------------------------------------------NAVBAR -->
        <h1>Actualizar Categoria</h1>
        <div class='container'>
            <form method='post' action='actualizarCategoria.jsp'>
        <%
            CategoriaDTO dto = new CategoriaDTO();
            String msg = "";
            dto.getEntidad().setIdCategoria(Integer.parseInt(request.getParameter("id")));
            dto.getEntidad().setNombreCategoria(request.getParameter("nombre"));
            dto.getEntidad().setDescripcionCategoria(request.getParameter("desc"));
            
            //FORMULARIO-----------------------------------------------------------------------FORMULARIO
            out.println("<label for='txtIdCategoria' class='form-label'>IdCategoria: </label>"
                        + "<input type='text' class='form-control' name='txtIdCategoria'"
                        + "value='"+dto.getEntidad().getIdCategoria()+"' readonly=readonly>"
                        
                        + "<label for='txtNombre' class='form-label'>Nombre: </label>"
                        + "<input type='text' class='form-control' name='txtNombre' required='required'"
                        + "value='"+dto.getEntidad().getNombreCategoria()+"'>"
                    
                        + "<label for='txtDescripcion' class='form-label'>Descripci&oacute;n: </label>"
                        + "<input type='text' class='form-control' name='txtDescripcion' required='required'"
                        + "value='"+dto.getEntidad().getDescripcionCategoria()+"'><hr>"
                        
                        +"<input type='submit' class='btn btn-primary' name='cmdEnviar' value='Enviar'>");
            //FORMULARIO-----------------------------------------------------------------------FORMULARIO
        %>
            </form>
        </div>
    </body>
</html>
