package BSCS.F19;

class base
{
public base()
{
System.out.println("No Argment Constructor Base");
}

public base(int v)
{
System.out.println("Overloaded Constructor Base");
}

}
class MyC extends base
{
private int t1,t2;
public MyC()
{
//super(10);

t1=10;
t2=20;
System.out.println("No Argment Constructor Child");

}

public MyC(int t1,int t2)
{

this.t1=t1;
this.t2=t2;
System.out.println("Overloaded Constructor");
}
public void show()
{
System.out.println("Values of a,b are::"+t1+","+t2);
}
 
public static void main(String[] ss)
{
MyC mc[]=new MyC[5];
for(int i=0;i<5;i++)
mc[i]=new MyC();

for(int j=0;j<5;j++)
mc[j].show();

}

}