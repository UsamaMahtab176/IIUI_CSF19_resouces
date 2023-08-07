
package ABC;

//import ABC.Base;
class Child extends Base

{
public Child()
{
System.out.println("No Argument Constructor Child");
}

public Child(int t)
{
super(10);
System.out.println("Overloaded Constructor Child");

}

public void cFun()
{
System.out.println("Function of child");
//System.out.println("Private::"+a;);
System.out.println("public::"+b);
System.out.println("Protected::"+c);
//System.out.println("Default::"+d);

}

/*public static void main(String ss[])
{
Child c=new Child(10);
c.bFun();
c.cFun();
}*/
}