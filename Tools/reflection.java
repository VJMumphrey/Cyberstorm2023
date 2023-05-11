import java.lang.reflect.*;
import java.util.Scanner;

class ReflectionTest{
    public static void main(String [] args) throws Exception{

        // Make class and instance of class
        String className = args[0].replace(".class", "");
        Object obj = Class.forName(className).newInstance(); 

        // Print name
        Class objclass = obj.getClass();
        System.out.println("Name : " + objclass.getName());

        // Print constructor
        Constructor objcon = objclass.getConstructor();
        System.out.println("Constructor : " + objcon.getName());

        // Field in the class
        System.out.println("---FIELDS---");
        Field[] fields = objclass.getDeclaredFields();
        int i = 0;
        for (Field f: fields){
            f.setAccessible(true);
            System.out.println("[" + i++ + "] " + f.getType() + " " + f.getName() + " = " + f.get(obj));
        }

        // Methods in the class
        System.out.println("---METHODS---");
        Method [] methods = objclass.getMethods();
        i = 0;
        for (Method m: methods){
            System.out.println("[" + i++ + "] " + m.getName());
        }

        // Declared Methods in the class
        System.out.println("---DECLARED METHODS---");
        Method[] allmethods = objclass.getDeclaredMethods();
        i = 0;
        for (Method m: allmethods){
            System.out.print("[" + i++ + "] " + m.getReturnType() + " " + m.getName() + "(");
            Parameter[] parameters = m.getParameters();
            for (Parameter p: parameters){
                System.out.print(p + ", ");
            }
            System.out.print(")\n");
        }
    }
}
