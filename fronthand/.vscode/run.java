 class Run implements Runnable  {
    void fun()
    {
        system.out.println("hi");

    }

public static void main(String[] args) {
    Run r = new Run();
   Thread t =new Thread(r);
 t.start();
 
}


}
