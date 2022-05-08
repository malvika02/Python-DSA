
public class fibo
{
    static int Fibo(int n){
        //base condition
        if (n < 2){
            return n;
        }
        return Fibo(n-1) + Fibo(n-2);
    }
    public static void main(String[] args){
        int n =5;
        System.out.println(Fibo(n));
    }
} 

    
