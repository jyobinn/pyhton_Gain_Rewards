package com.example.demo;

import java.util.ArrayList;
import java.util.List;

public class DemoTest {

    public static List add(List a) {
        a.add(1);
        System.out.println(a);
        return a;
    }

    public static List add2(List a) {
        List b = new ArrayList();
        b.add(2);
        a = b;
        System.out.println(a);
        return a;
    }

    public static void main(String[] args) {
        List b = new ArrayList();
        b.add(9);
        add(b);
        System.out.println(b);
        add2(b);
        System.out.println(b);
    }
}
