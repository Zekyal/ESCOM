<%@page import="com.ipn.mx.modelo.dto.ProductoDTO"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Actualizar Producto</title>
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
        <h1>Actualizar Producto</h1>
        <div class='container'>
            <form method='post' action='actualizarProducto.jsp'>
                <%
                    ProductoDTO dto = new ProductoDTO();
                    dto.getEntidad().setIdProducto(Integer.parseInt(request.getParameter("id")));
                    dto.getEntidad().setNombreProducto(request.getParameter("nombre"));
                    dto.getEntidad().setPrecioProducto(Double.parseDouble(request.getParameter("precio")));
                    dto.getEntidad().setExistenciaProducto(Integer.parseInt(request.getParameter("exist")));
                    dto.getEntidad().setDescripcionProducto(request.getParameter("desc"));
                    dto.getEntidad().setIdCategoria(Integer.parseInt(request.getParameter("idCat")));
                    out.println("<label for='txtIdProducto' class='form-label'>IdProducto: </label>"
                            + "<input type='number' class='form-control' name='txtIdProducto' required='required'"
                            + "value='" + dto.getEntidad().getIdProducto() + "' readonly=readonly>"
                            + "<label for='txtNombre' class='form-label'>Nombre: </label>"
                            + "<input type='text' class='form-control' name='txtNombre' required='required'"
                            + "value='" + dto.getEntidad().getNombreProducto() + "'>"
                            + "<label for='txtPrecio' class='form-label'>Precio: </label>"
                            + "<input step='0.01' type='number' class='form-control' name='txtPrecio' id='txtPrecio' placeholder='100' required='required'"
                            + "value='" + dto.getEntidad().getPrecioProducto() + "'>"
                            + "<label for='txtExistencia' class='form-label'>Existencia: </label>"
                            + "<input type='number' class='form-control' name='txtExistencia' id='txtExistencia' placeholder='20' required='required'"
                            + "value='" + dto.getEntidad().getExistenciaProducto() + "'>"
                            + "<label for='txtDescripcion' class='form-label'>Descripci&oacute;n: </label>"
                            + "<input type='text' class='form-control' name='txtDescripcion' required='required'"
                            + "value='" + dto.getEntidad().getDescripcionProducto() + "'><hr>"
                            + "<label for='txtIdCategoria' class='form-label'>ID Categoria: </label>"
                            + "<input type='number' class='form-control' name='txtIdCategoria' id='txtIdCategoria' placeholder='1' required='required'"
                            + "value='" + dto.getEntidad().getIdCategoria() + "'>"
                            + "<input type='submit' class='btn btn-primary' name='cmdEnviar' value='Enviar'>");
                %>
            </form>
        </div>
    </body>
</html>
