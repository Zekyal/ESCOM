<%@page import="com.ipn.mx.modelo.dto.CategoriaDTO"%>
<%@page import="com.ipn.mx.modelo.dto.ProductoDTO"%>
<%@page import="java.util.List"%>
<%@page import="com.ipn.mx.modelo.dao.CategoriaDAO"%>
<%@page import="com.ipn.mx.modelo.dao.ProductoDAO"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Productos</title>
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
                                <a class='nav-link disabled'aria-current='page' href='listaDeProductos.jsp'>Mostrar Productos</a>
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
        <h1>Productos</h1>
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
                        <td></td>
                        <td></td>
                    </tr>
                </thead>
                <%
                    ProductoDAO dao = new ProductoDAO();
                    CategoriaDAO daoc = new CategoriaDAO();//---------
                    List resultado = dao.readAll();
                    List resultadoc = daoc.readAll();//---------
                    for (int i = 0; i < resultado.size(); i++) {
                        ProductoDTO dto = (ProductoDTO) resultado.get(i);
                        out.println("<tr>");
                        out.println("<td><a href='verProducto.jsp?id=" + dto.getEntidad().getIdProducto() + "'class='btn  btn-warning'>"
                                + dto.getEntidad().getIdProducto() + "</a></td>");
                        out.println("<td>" + dto.getEntidad().getNombreProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getPrecioProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getExistenciaProducto() + "</td>");
                        out.println("<td>" + dto.getEntidad().getDescripcionProducto() + "</td>");
                        out.println("<td><a href='/ProyectoBase3CM18-V2/Categorias/verCategoria.jsp?id=" + dto.getEntidad().getIdCategoria() + "'class='btn  btn-warning'>"
                                + dto.getEntidad().getIdCategoria() + "</a></td>");
                        CategoriaDTO dtoc = (CategoriaDTO) resultadoc.get(dto.getEntidad().getIdCategoria() - 1);//--------- se le pone -1 a esta lectura debido a que el indide del Resulset esta desfasado en 1
                        out.println("<td>" + dtoc.getEntidad().getNombreCategoria() + "</td>");//---------
                        out.println("<td><a href='eliminarProducto.jsp?id=" + dto.getEntidad().getIdProducto() + "' class='btn  btn-danger'>Eliminar</a></td>");
                        out.println("<td><a href='actualizarProductoForm.jsp?id=" + dto.getEntidad().getIdProducto()
                                + "&nombre=" + dto.getEntidad().getNombreProducto()
                                + "&precio=" + dto.getEntidad().getPrecioProducto()
                                + "&exist=" + dto.getEntidad().getExistenciaProducto()
                                + "&desc=" + dto.getEntidad().getDescripcionProducto()
                                + "&idCat=" + dto.getEntidad().getIdCategoria() + "'"
                                + "class='btn  btn-success'>Actualizar</a></td>");
                        out.println("</tr>");
                    }
                %>
            </table>
            <a href="nuevoProductoForm.jsp" class="btn btn-primary">Nuevo Producto</a>
        </div>
    </body>
</html>
