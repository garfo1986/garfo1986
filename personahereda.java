public class personahereda {

    public class Main {
        public static void main(String[] args) throws Exception {
            
            cliente cliente1 = new cliente();
            cliente1.credito = 800;
            cliente1.edad = 36;
            cliente1.telefono = 6143200;
            System.out.println(cliente1.edad);
            System.out.println(cliente1.telefono);
            System.out.println(cliente1.credito);
    
            trabajador trabajador1 = new trabajador();
            trabajador1.salario = 2650;
            trabajador1.edad =37;
            trabajador1.telefono = 65540253;
            System.out.println(trabajador1.salario);
            System.out.println(trabajador1.edad);
            System.out.println(trabajador1.telefono);
        }
    static class person{
        int edad;
        String name;
        int telefono;   
    }
    static class cliente extends person{
        int credito;
    }
    static class trabajador extends person{
        int salario;
    }
 }
          