<%@page import="com.ipn.mx.modelo.dto.ProductoDTO"%>
<%@page import="com.ipn.mx.modelo.dao.ProductoDAO"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <META HTTP-EQUIV='REFRESH' CONTENT='1;URL=listaDeProductos.jsp'>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Eliminar Producto</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" ></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>
    </head>
    <body class="p-3 mb-2 bg-dark text-white">
        <%
            ProductoDAO dao = new ProductoDAO();
            ProductoDTO dto = new ProductoDTO();
            dto.getEntidad().setIdProducto(Integer.parseInt(request.getParameter("id")));
                dto = dao.read(dto);
                out.println("<h2>El elemento ''"+ dto.getEntidad().getNombreProducto()+ "'' fue eliminado</h2>");
                dao.delete(dto);
        %>
    </body>
</html>
