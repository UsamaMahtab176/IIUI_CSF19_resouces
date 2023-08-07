

package ABC;

class Base
{
private int a;
public int b;
protected int c;
int d;

public Base() 
{
a=b=c=d=400;
System.out.println("No Argument Constructor Base");
}

public Base(int v) 
{
a=10;
b=20; 
c=30;
d=100;
System.out.println("Overloaded Constructor Base");
}

public void bFun()
{
System.out.println("Function of Base");
}
}