<%-- 
    Document   : TablasDeMultiplicar
    Created on : 24 nov. 2021, 08:22:57
    Author     : genzo
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Tablas De Multiplicar</title>
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
                    <a class="navbar-brand" href="index.jsp">Proyecto Base V2</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class='nav-item'>
                                <a class='nav-link disabled' aria-current='page' href='TablaDeMultiplicar.jsp'>TablaDeMultiplicar</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='Productos/listaDeProductos.jsp'>Mostrar Productos</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='Categorias/listaDeCategorias.jsp'>Mostrar Categorias</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='Categorias/nuevaCategoriaForm.jsp'>Crear Categoria</a>
                            </li>
                            <li class='nav-item'>
                                <a class='nav-link active'aria-current='page' href='Productos/nuevoProductoForm.jsp'>Crear Producto</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
        <!-- NAVBAR---------------------------------------------------------------NAVBAR -->
        <h1>Tablas De Multiplicar</h1>
        <table style="text-align:center;" class="table table-dark table-hover">
            <%
                for (int i = 1; i <= 10; i++) {
                    out.println("<tr>");
                    for (int j = 1; j <= 10; j++) {
                        out.println("<td>" + (i * j) + "</td>");
                    }
                    out.println("</tr>");
                }
            %>
        </table>
        <%int var=14;%>
        <h1>La variable de prueba vale: <%=var%></h1>
    </body>
</html>
