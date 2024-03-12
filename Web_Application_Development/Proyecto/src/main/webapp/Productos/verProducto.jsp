<%@page import="com.ipn.mx.modelo.dao.CategoriaDAO"%>
<%@page import="com.ipn.mx.modelo.dto.CategoriaDTO"%>
<%@page import="com.ipn.mx.modelo.dto.ProductoDTO"%>
<%@page import="com.ipn.mx.modelo.dao.ProductoDAO"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Ver Categoria</title>
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
                                <a class='nav-link active'aria-current='page' href='listaDeProductos.jsp'>Mostrar Productos</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='/ProyectoBase3CM18-V2/Categorias/listaDeCategorias.jsp'>Mostrar Categorias</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='/ProyectoBase3CM18-V2/Categorias/nuevaCategoriaForm.jsp'>Crear Categoria</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='nuevoProductoForm.jsp'>Crear Producto</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
        <!-- NAVBAR---------------------------------------------------------------NAVBAR -->
        <div class='table-responsive'>
            <table class='table table-dark table-hover'>
                <thead>
                    <tr>
                        <td>Clave</td>
                        <td>Nombre</td>
                        <td>Precio</td>
                        <td>Existencia</td>
                        <td>Descripcion</td>
                        <td>ID_Categoria</td>
                        <td>Categoria</td>
                    </tr>
                </thead>
                <%
                    ProductoDAO dao = new ProductoDAO();
                    ProductoDTO dto = new ProductoDTO();
                    CategoriaDTO dtoc = new CategoriaDTO();
                    CategoriaDAO daoc = new CategoriaDAO();
                    dto.getEntidad().setIdProducto(Integer.parseInt(request.getParameter("id")));
                    dto = dao.read(dto);
                    out.println("<tr>");
                    if (dto != null) {
                        dtoc.getEntidad().setIdCategoria(dto.getEntidad().getIdCategoria());
                        dtoc = daoc.read(dtoc);
                        out.println("<td>" + dto.getEntidad().getIdProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getNombreProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getPrecioProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getExistenciaProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getDescripcionProducto() + "</td>");
                        out.println("<td><a href='/ProyectoBase3CM18-V2/Categorias/verCategoria.jsp?id=" + dto.getEntidad().getIdCategoria() + "'class='btn  btn-warning'>"
                                + dto.getEntidad().getIdCategoria() + "</a></td>");
                        out.println("<td>" + dtoc.getEntidad().getNombreCategoria() + "</td>");
                    }
                    out.println("</tr>");
                    out.println("<tr><td COLSPAN='7'>");
                    out.println("<img src='/ProyectoBase3CM18/images/img.png' class='rounded mx-auto d-block' "
                            + "alt='" + dto.getEntidad().getDescripcionProducto() + "'"
                            + "width='400' height='400'>"
                    );

                    out.println("</td></tr>");
                %>
            </table>
        </div>
    </body>
</html>
