/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ipn.mx.modelo.dao;

import com.ipn.mx.modelo.dto.ProductoDTO;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author genzo
 */
public class ProductoDAO {
    private static final String SQL_INSERT = "insert into producto (nombreproducto, descripcionproducto, precio, existencia, idcategoria) values (?, ?, ?, ?, ?);";
    private static final String SQL_INSERT_ID = "insert into producto (idproducto, nombreproducto, descripcionproducto, precio, existencia, idcategoria) values (?, ?, ?, ? , ?, ?);";
    private static final String SQL_UPDATE = "update producto set nombreproducto = ?, descripcionproducto =?, precio =?, existencia=?, idcategoria=? where idproducto = ?;";
    private static final String SQL_DELETE = "delete from producto where idproducto = ?;";
    private static final String SQL_SELECT = "select * from producto where idproducto = ?;";
    private static final String SQL_SELECT_ALL = "select * from producto order by idproducto asc;";

    private Connection conexion;

    private void obtenerConexion() {
        String usuario = "postgres";
        String clave = "root";
        String url = "jdbc:postgresql://localhost:5432/Base3CM18";
        String driverPostgreSql = "org.postgresql.Driver";
        try {
            Class.forName(driverPostgreSql);
            conexion = DriverManager.getConnection(url, usuario, clave);
        } catch (ClassNotFoundException | SQLException e) {
            Logger.getLogger(CategoriaDAO.class.getName()).log(Level.SEVERE, null, e);
        }
    }
    
    public void create(ProductoDTO dto) throws SQLException {
        obtenerConexion();
        try (PreparedStatement ps = conexion.prepareStatement(SQL_INSERT)) {
            ps.setString(1, dto.getEntidad().getNombreProducto());
            ps.setString(2, dto.getEntidad().getDescripcionProducto());
            ps.setDouble(3, dto.getEntidad().getPrecioProducto());
            ps.setInt(4, dto.getEntidad().getExistenciaProducto());
            ps.setInt(5, dto.getEntidad().getIdCategoria());
            ps.executeUpdate();
        } finally {
            if (conexion != null) {
                conexion.close();
            }
        }
    }
    
    public void insertID(ProductoDTO dto) throws SQLException {
        obtenerConexion();
        try (PreparedStatement ps = conexion.prepareStatement(SQL_INSERT_ID)) {
            ps.setInt(1, dto.getEntidad().getIdCategoria());
            ps.setString(2, dto.getEntidad().getNombreProducto());
            ps.setString(3, dto.getEntidad().getDescripcionProducto());
            ps.setDouble(4, dto.getEntidad().getPrecioProducto());
            ps.setInt(5, dto.getEntidad().getExistenciaProducto());
            ps.setInt(6, dto.getEntidad().getIdCategoria());
            ps.executeUpdate();
        } finally {
            if (conexion != null) {
                conexion.close();
            }
        }
    }

    public void update(ProductoDTO dto) throws SQLException {
        obtenerConexion();
        PreparedStatement ps = null;
        try {
            ps = conexion.prepareStatement(SQL_UPDATE);
            ps.setString(1, dto.getEntidad().getNombreProducto());
            ps.setString(2, dto.getEntidad().getDescripcionProducto());
            ps.setDouble(3, dto.getEntidad().getPrecioProducto());
            ps.setInt(4, dto.getEntidad().getExistenciaProducto());
            ps.setInt(5, dto.getEntidad().getIdCategoria());
            ps.setInt(6, dto.getEntidad().getIdProducto());
            ps.executeUpdate();
        } finally {
            if (ps != null) {
                ps.close();
            }
            if (conexion != null) {
                conexion.close();
            }
        }
    }

    public void delete(ProductoDTO dto) throws SQLException {
        obtenerConexion();
        PreparedStatement ps = null;
        try {
            ps = conexion.prepareStatement(SQL_DELETE);
            ps.setInt(1, dto.getEntidad().getIdProducto());
            ps.executeUpdate();
        } finally {
            if (ps != null) {
                ps.close();
            }
            if (conexion != null) {
                conexion.close();
            }
        }
    }

    public ProductoDTO read(ProductoDTO dto) throws SQLException{
        obtenerConexion();
        PreparedStatement ps = null;
        ResultSet rs =null;
        try{
            ps = conexion.prepareStatement(SQL_SELECT);
            ps.setInt(1, dto.getEntidad().getIdProducto());
            rs = ps.executeQuery();
            List resultados = obtenerResultados(rs);
            if(resultados.size() > 0){return (ProductoDTO) resultados.get(0);}
            else{return null;}
        }finally{
            if (rs != null) rs.close();
            if (ps != null) ps.close();
            if (conexion != null) conexion.close();
        }
    }
    
    public List readAll() throws SQLException{
        obtenerConexion();
        PreparedStatement ps = null;
        ResultSet rs = null;
        try{
            ps = conexion.prepareStatement(SQL_SELECT_ALL);
            rs = ps.executeQuery();
            List resultados = obtenerResultados(rs);
            if (resultados.size() > 0){
                return resultados;
            }else{
                return null;
            }
        }finally{
            if (rs != null) rs.close();
            if (ps != null) ps.close();
            if (conexion != null) conexion.close();
        }
    }
    
    private List obtenerResultados(ResultSet rs) throws SQLException {
        List resultados = new ArrayList();
        while(rs.next()){
            ProductoDTO dto = new ProductoDTO();
            dto.getEntidad().setIdProducto(rs.getInt("idProducto"));
            dto.getEntidad().setNombreProducto(rs.getString("nombreProducto"));
            dto.getEntidad().setDescripcionProducto(rs.getString("descripcionProducto"));
            dto.getEntidad().setPrecioProducto(rs.getDouble("precio"));
            dto.getEntidad().setExistenciaProducto(rs.getInt("existencia"));
            dto.getEntidad().setIdCategoria(rs.getInt("idcategoria"));
            resultados.add(dto);
        }
        return resultados;
    }
    
    public static void main(String[] args) {
        ProductoDTO dto = new ProductoDTO();
        dto.getEntidad().setIdProducto(4);
        dto.getEntidad().setNombreProducto("relleno");
        dto.getEntidad().setDescripcionProducto("descripcion de relleno");
        dto.getEntidad().setPrecioProducto(0.99);
        dto.getEntidad().setExistenciaProducto(1);
        dto.getEntidad().setIdCategoria(10);
        ProductoDAO dao = new ProductoDAO();

        try {
            //for(int i=0; i<6; i++){dao.create(dto);}
            //dao.create(dto);
            //dao.insertID(dto);
            //dao.update(dto);
            //dao.delete(dto);
            System.out.println(dao.read(dto).toString());
            //System.out.println(dao.readAll().toString());
        } catch (SQLException ex) {
            Logger.getLogger(CategoriaDAO.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.exit(0);
    }
}
