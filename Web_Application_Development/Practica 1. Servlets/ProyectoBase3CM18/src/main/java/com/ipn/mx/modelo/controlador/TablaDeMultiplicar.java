/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ipn.mx.modelo.controlador;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author genzo
 */
@WebServlet(name = "TablaDeMultiplicar", urlPatterns = {"/TablaDeMultiplicar"})
public class TablaDeMultiplicar extends HttpServlet {

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
            out.println("<title>Servlet Tabla De Multiplicar</title>");
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
            out.println("<div class='table-responsive'>");
            out.println("<h1>Servlet Tabla De Multiplicar at " + request.getContextPath() + "</h1>");
            out.println("<hr>");
            out.println("<table class='table table-success table-striped'>");
                for(int i=1; i<=10; i++ ){
                    out.println("<tr>");
                        for(int j=1;j<=10;j++){
                            out.println("<td class='center'>"+(i*j)+"</td>");
                        }
                    out.println("</tr>");
                }
            out.println("</table>");
            out.println("<div>");
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
