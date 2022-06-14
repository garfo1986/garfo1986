public class persona{

    public static void main(String[] args){
        persona1 person = new persona1();
            person.setedad(18);
            person.setnombre("Juan");
            person.settelefono(38042);
            System.out.println(person.edad);
            System.out.println(person.nombre);
            System.out.println(person.telefono);

    }
static class persona1{
    private int edad;
    private String nombre;
    private int telefono;

    private void setedad(int edad){
        this.edad = edad;
    
    }
    private int getedad(){
        return this.edad;
    }
    
    private void setnombre(String nombre){
        this.nombre = nombre;
        
    }
    private String getnombre(){
        return this.nombre;
    }
    private void settelefono(int telefono){
        this.telefono = telefono;
    }
    private int gettelefono(){
        return this.telefono;
    } 
    }

}