/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ipn.mx.modelo.controlador.categoria;

import com.ipn.mx.modelo.dao.CategoriaDAO;
import com.ipn.mx.modelo.dao.ProductoDAO;
import com.ipn.mx.modelo.dto.CategoriaDTO;
import com.ipn.mx.modelo.dto.ProductoDTO;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author genzo
 */
@WebServlet(name = "VerCategoria", urlPatterns = {"/VerCategoria"})
public class VerCategoria extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Ver Categoria</title>");
            //out.println("<META HTTP-EQUIV='REFRESH' CONTENT='3;URL=MostrarCategorias'>");
            out.println("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css' rel='stylesheet'>");
            out.println("<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js'></script>");
            
            out.println("<script src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js'></script>");
            out.println("<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js'></script>");
            out.println("</head>");
            out.println("<body>");
            //NAVBAR-------------------------------------------------------------------------------NAVBAR
            out.println("<div><nav class='navbar navbar-expand-lg navbar-light bg-light'>"
                + "<div class='container-fluid'>"
                    + "<a class='navbar-brand' href='index.html'>Home</a>"
                    + "<button class='navbar-toggler' type='button' data-bs-toggle='collapse' data-bs-target='#navbarNav' aria-controls='navbarNav' aria-expanded='false' aria-label='Toggle navigation'>"
                        + "<span class='navbar-toggler-icon'></span>"
                    + "</button>"
                    + "<div class='collapse navbar-collapse' id='navbarNav'>"
                        + "<ul class='navbar-nav'>"
                            + "<li class='nav-item'>"
                                + "<a class='nav-link active' aria-current='page' href='TablaDeMultiplicar'>TablaDeMultiplicar</a>"
                            + "</li>"
                            + "<li class='nav-item'>"
                                + "<a class='nav-link' href='MostrarProductos'>Mostrar Productos</a>"
                            + "</li>"
                            + "<li class='nav-item'>"
                                + "<a class='nav-link' href='MostrarCategorias'>Mostrar Categorias</a>"
                            + "</li>"
                            + "<li class='nav-item'>"
                                + "<a class='nav-link' href='categoriaForm.html'>Crear Categoria</a>"
                            + "</li>"
                            + "<li class='nav-item'>"
                                + "<a class='nav-link' href='productoForm.html'>Crear Producto</a>"
                            + "</li>"
                        + "</ul>"
                    + "</div>"
                + "</div>"
            + "</nav></div>");
            //NAVBAR-------------------------------------------------------------------------------NAVBAR
            out.println("<div class='container'>");
            out.println("<table class='table table-success table-striped'>");
            out.println("<thead><tr>"
                    + "<td>Clave</td>"
                    + "<td>Nombre</td>"
                    + "<td>Descripcion</td>"
                    + "</tr></thead>");
            CategoriaDAO dao = new CategoriaDAO();
            CategoriaDTO dto = new CategoriaDTO();
            dto.getEntidad().setIdCategoria(Integer.parseInt(request.getParameter("id")));
            try {
                dto = dao.read(dto);
            } catch (SQLException ex) {
                Logger.getLogger(VerCategoria.class.getName()).log(Level.SEVERE, null, ex);
            }
            out.println("<tr>");
            if(dto!= null){
                out.println("<td>"+dto.getEntidad().getIdCategoria()+"</td>");
                out.println("<td>"+dto.getEntidad().getNombreCategoria()+"</td>");
                out.println("<td>"+dto.getEntidad().getDescripcionCategoria()+"</td>");
            }
            out.println("</tr></table>");
            //------------------------------------------------------------------------------------------------
            out.println("<div class='table-responsive'>");
            out.println("<hr>");
            out.println("");
            out.println("<table class='table table-success table-striped'>");
            out.println("<thead><tr>"
                    + "<td>Clave</td>"
                    + "<td>Nombre</td>"
                    + "<td>Precio</td>"
                    + "<td>Existencia</td>"
                    + "<td>Descripcion</td>"
                    + "</tr></thead>");
            ProductoDAO daop=new ProductoDAO();
            try {
                List resultado = daop.readAll();
                for(int i=0; i<resultado.size(); i++ ){
                    ProductoDTO dtop = (ProductoDTO) resultado.get(i);
                    if(dtop.getEntidad().getIdCategoria()==dto.getEntidad().getIdCategoria()){
                        out.println("<tr>");
                        out.println("<td><a href='VerProducto?id="+dtop.getEntidad().getIdProducto()+"'class='btn  btn-warning'>"
                                + dtop.getEntidad().getIdProducto()+ "</a></td>");
                        out.println("<td>"+dtop.getEntidad().getNombreProducto()+"</td>");
                        out.println("<td>"+dtop.getEntidad().getPrecioProducto()+"</td>");
                        out.println("<td>"+dtop.getEntidad().getExistenciaProducto()+"</td>");
                        out.println("<td>"+dtop.getEntidad().getDescripcionProducto()+"</td>");
                        out.println("</tr>");
                    }
                }
            } catch (SQLException ex) {
                Logger.getLogger(MostrarCategorias.class.getName()).log(Level.SEVERE, null, ex);
            }
            out.println("</table>");
            out.println("<div>");
            //------------------------------------------------------------------------------------------------
            out.println("</div>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
