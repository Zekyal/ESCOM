<%@page import="com.ipn.mx.modelo.dto.CategoriaDTO"%>
<%@page import="java.util.List"%>
<%@page import="com.ipn.mx.modelo.dao.CategoriaDAO"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Lista de categorias</title>
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
                                <a class='nav-link disabled'aria-current='page' href='listaDeCategorias.jsp'>Mostrar Categorias</a>
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
        <h1>Categorias</h1>
        <div class='table-responsive'>
            <table class='table table-dark table-hover'>
                <thead>
                    <tr>
                        <td>Clave</td>
                        <td>Nombre</td>
                        <td>Descripcion</td>
                        <td></td>
                        <td></td>
                    </tr>
                </thead>
                <%
                CategoriaDAO dao=new CategoriaDAO();

                    List resultado = dao.readAll();
                    for(int i=0; i<resultado.size(); i++ ){
                        CategoriaDTO dto = (CategoriaDTO) resultado.get(i);
                        out.println("<tr>");
                        out.println("<td><a href='verCategoria.jsp?id="+dto.getEntidad().getIdCategoria()+"'class='btn  btn-warning'>");
                        out.println(dto.getEntidad().getIdCategoria());
                        out.println("</a></td>");
                        out.println("<td>"+dto.getEntidad().getNombreCategoria()+"</td>");
                        out.println("<td>"+dto.getEntidad().getDescripcionCategoria()+"</td>");
                        out.println("<td><a href='eliminarCategoria.jsp?id="+dto.getEntidad().getIdCategoria()+"' class='btn  btn-danger'>Eliminar</a></td>");
                        out.println("<td><a href='actualizarCategoriaForm.jsp?id="+dto.getEntidad().getIdCategoria()
                                                                +"&nombre="+dto.getEntidad().getNombreCategoria()
                                                                +"&desc="+dto.getEntidad().getDescripcionCategoria()+"'"
                                                                + "class='btn  btn-success'>Actualizar</a></td>");
                        out.println("</tr>");
                    }
            %>
            </table>
            <a href="nuevaCategoriaForm.jsp" class="btn btn-primary">Nueva Categoria</a>
        </div>
    </body>
</html>
