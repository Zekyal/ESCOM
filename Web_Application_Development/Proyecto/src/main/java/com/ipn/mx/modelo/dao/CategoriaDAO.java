/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ipn.mx.modelo.dao;

import com.ipn.mx.modelo.dto.CategoriaDTO;
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
 * @author darkdestiny
 */
public class CategoriaDAO {

    private static final String SQL_INSERT = "insert into Categoria (nombreCategoria, descripcionCategoria) values (? , ?);";
    private static final String SQL_INSERT_ID = "insert into Categoria (idcategoria, nombreCategoria, descripcionCategoria) values (?, ? , ?);";
    private static final String SQL_UPDATE = "update Categoria set nombreCategoria = ?, descripcionCategoria =? where idCategoria = ?;";
    private static final String SQL_DELETE = "delete from Categoria where idCategoria = ?;";
    private static final String SQL_SELECT = "select * from Categoria where idCategoria = ?;";
    private static final String SQL_SELECT_ALL = "select * from Categoria order by idCategoria asc;";

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

    public void create(CategoriaDTO dto) throws SQLException {
        obtenerConexion();
        try (PreparedStatement ps = conexion.prepareStatement(SQL_INSERT)) {
            ps.setString(1, dto.getEntidad().getNombreCategoria());
            ps.setString(2, dto.getEntidad().getDescripcionCategoria());
            ps.executeUpdate();
        } finally {
            if (conexion != null) {
                conexion.close();
            }
        }
    }
    
    public void insertID(CategoriaDTO dto) throws SQLException {
        obtenerConexion();
        try (PreparedStatement ps = conexion.prepareStatement(SQL_INSERT_ID)) {
            ps.setInt(1, dto.getEntidad().getIdCategoria());
            ps.setString(2, dto.getEntidad().getNombreCategoria());
            ps.setString(3, dto.getEntidad().getDescripcionCategoria());
            ps.executeUpdate();
        } finally {
            if (conexion != null) {
                conexion.close();
            }
        }
    }

    public void update(CategoriaDTO dto) throws SQLException {
        obtenerConexion();
        PreparedStatement ps = null;
        try {
            ps = conexion.prepareStatement(SQL_UPDATE);
            ps.setString(1, dto.getEntidad().getNombreCategoria());
            ps.setString(2, dto.getEntidad().getDescripcionCategoria());
            ps.setInt(3, dto.getEntidad().getIdCategoria());
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

    public void delete(CategoriaDTO dto) throws SQLException {
        obtenerConexion();
        PreparedStatement ps = null;
        try {
            ps = conexion.prepareStatement(SQL_DELETE);
            ps.setInt(1, dto.getEntidad().getIdCategoria());
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

    public CategoriaDTO read(CategoriaDTO dto) throws SQLException{
        obtenerConexion();
        PreparedStatement ps = null;
        ResultSet rs =null;
        try{
            ps = conexion.prepareStatement(SQL_SELECT);
            ps.setInt(1, dto.getEntidad().getIdCategoria());
            rs = ps.executeQuery();
            List resultados = obtenerResultados(rs);
            if(resultados.size() > 0){return (CategoriaDTO) resultados.get(0);}
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
            CategoriaDTO dto = new CategoriaDTO();
            dto.getEntidad().setIdCategoria(rs.getInt("idCategoria"));
            dto.getEntidad().setNombreCategoria(rs.getString("nombreCategoria"));
            dto.getEntidad().setDescripcionCategoria(rs.getString("descripcionCategoria"));
            resultados.add(dto);
        }
        return resultados;
    }
    
    public static void main(String[] args) {
        CategoriaDTO dto = new CategoriaDTO();
        dto.getEntidad().setNombreCategoria("relleno");
        dto.getEntidad().setDescripcionCategoria("relleno para pruebas");
        dto.getEntidad().setIdCategoria(5);
        CategoriaDAO dao = new CategoriaDAO();

        try {
            //for(int i=0; i<10; i++){dao.create(dto);}
            //dao.create(dto);
            //dao.insertID(dto);
            //dao.update(dto);
            //dao.delete(dto);
            //System.out.println(dao.read(dto).toString());
            System.out.println(dao.readAll().toString());
        } catch (SQLException ex) {
            Logger.getLogger(CategoriaDAO.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.exit(0);
    }
}
