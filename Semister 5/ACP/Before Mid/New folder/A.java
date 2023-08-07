class A
{
private int a;

public A()
{
System.out.println("In constructor");
a=20;
}
public void f()
{
System.out.println("In function f()");
System.out.println("In function f()::The value of a is::"+a);
}
public static void main(String[] s)
{
A obj=new A();
obj.a=40;
obj.f();
}
}
