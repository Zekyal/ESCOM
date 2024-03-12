<%@page import="com.ipn.mx.modelo.dao.CategoriaDAO"%>
<%@page import="com.ipn.mx.modelo.dto.CategoriaDTO"%>
<%@page import="com.ipn.mx.modelo.dto.ProductoDTO"%>
<%@page import="com.ipn.mx.modelo.dao.ProductoDAO"%>
<%@page import="java.util.List"%>
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
                                <a class='nav-link active'aria-current='page' href='/royectoBase3CM18-V2/Productos/listaDeProductos.jsp'>Mostrar Productos</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='listaDeCategorias.jsp'>Mostrar Categorias</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='nuevaCategoriaForm.jsp'>Crear Categoria</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='/royectoBase3CM18-V2/Productos/nuevoProductoForm.jsp'>Crear Producto</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
        <!-- NAVBAR---------------------------------------------------------------NAVBAR -->
        <%
            CategoriaDAO dao = new CategoriaDAO();
            CategoriaDTO dto = new CategoriaDTO();
            dto.getEntidad().setIdCategoria(Integer.parseInt(request.getParameter("id")));
            dto = dao.read(dto);
            if (dto != null) {
                out.println("<h1>Categoria: " + dto.getEntidad().getNombreCategoria() + "</h1>");
            }%>
        <div class='table-responsive'>
            <table class='table table-dark table-hover'>
                <thead><tr>
                        <td>Clave</td>
                        <td>Nombre</td>
                        <td>Precio</td>
                        <td>Existencia</td>
                        <td>Descripcion</td>
                    </tr></thead>
                    <%
                        ProductoDAO daop = new ProductoDAO();
                        List resultado = daop.readAll();
                        for (int i = 0; i < resultado.size(); i++) {
                            ProductoDTO dtop = (ProductoDTO) resultado.get(i);
                            if (dtop.getEntidad().getIdCategoria() == dto.getEntidad().getIdCategoria()) {
                                out.println("<tr>");
                                out.println("<td><a href='/ProyectoBase3CM18-V2/Productos/verProducto.jsp?id=" + dtop.getEntidad().getIdProducto() + "'class='btn  btn-warning'>"
                                        + dtop.getEntidad().getIdProducto() + "</a></td>");
                                out.println("<td>" + dtop.getEntidad().getNombreProducto() + "</td>");
                                out.println("<td>" + dtop.getEntidad().getPrecioProducto() + "</td>");
                                out.println("<td>" + dtop.getEntidad().getExistenciaProducto() + "</td>");
                                out.println("<td>" + dtop.getEntidad().getDescripcionProducto() + "</td>");
                                out.println("</tr>");
                            }
                        }
                    %>
            </table>
        </div>
    </body>
</html>
