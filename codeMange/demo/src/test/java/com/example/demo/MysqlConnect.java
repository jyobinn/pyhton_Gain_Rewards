package com.example.demo;

import java.sql.*;

public class MysqlConnect {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        String URL="jdbc:mysql://192.168.238.1:3306/test";
        String USER="root";
        String PASSWORD="Test234";
        //1.加载驱动程序
        Class.forName("com.mysql.cj.jdbc.Driver");
        //2.获得数据库链接
        Connection conn=DriverManager.getConnection(URL, USER, PASSWORD);
        //3.通过数据库的连接操作数据库，实现增删改查（使用Statement类）
        Statement st=conn.createStatement();
        ResultSet rs=st.executeQuery("select 1 FROM dual");
        //4.处理数据库的返回结果(使用ResultSet类)
//        while(rs.next()){
//            System.out.println(rs.getString("name")+" "
//                    +rs.getString("value"));
//        }

        //关闭资源
        rs.close();
        st.close();
        conn.close();
    }
}
