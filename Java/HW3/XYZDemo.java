package HW3;

class XYZ //A. class and G. Encapsulation (because it contains multiple instance variables and methods)
{
    double a; //E. Data members/attributes/properties/instance variable
    double b; //E. Data members/attributes/properties/instance variable
    double c; //E. Data members/attributes/properties/instance variable
    double d; //E. Data members/attributes/properties/instance variable
    XYZ() //I. Constructors and their types and K. Polymorphism with constructors
    {
        a = 0.0;
        b = 1.0;
        c = 0.0;
        d = 1.0;
    }
    XYZ(double a) //D. Constructors and their types and J. Constructor overloading(second constructor) and
    //K. Polymorphism with constructors
    {
        this.a = this.b = this.c = this.d = a;
    }
    XYZ(double a1, double a2, double a3, double a4) //D. Constructors and their types and 
    //J. Constructor overloading(third constructor) and K. Polymorphism with constructors
    {
        a = a1;
        b = a2;
        c = a3;
        d = a4;
    }
    void prodAll() //F. Methods/member function/actions/behavior
    {
        this.d = this.a*this.b*this.c;  //Explain this keyword role here
        //The this keyword refers to the current object in this method in the 
        //XYZ class, meaning the object created using the XYZ class
    }
    void printProdAll() //F. Methods/member function/actions/behavior
    {
        System.out.println("a = "+this.a+" b = "+b+" c = "+this.c+" \nproduct d = "+d);
    }
}

class XYZDemo //A. class
{
    public static void main(String args[]) //F. Methods/member function/actions/behavior
    {
        XYZ A1; //B. A1 is a reference to an object and C. Creating a reference to an object but not linked yet
        A1 = new XYZ(); //D. Object creation
        XYZ A2 = new XYZ(); //B. A2 is a reference to an object and D. object creation
        XYZ A3; //B. A3 is a reference to an object and C. Creating a reference to an object but not linked yet
        A3 = new XYZ(10); //D. object creation
        XYZ A4 = new XYZ(1,2,3,4); //A4 is a reference to an object and D. object creation
        XYZ A5 = A4; //B. A5 is a reference to an object and H. Making two reference variables or class instances pointing
        //to the same object memory
        A1.printProdAll();
        A2.printProdAll();
        A3.printProdAll();
        A4.printProdAll();  //why identical results here and from next line
        A5.printProdAll();	//When the object A5 was created, instead of allocating new 
        A1.prodAll();		//space in the memory for it, it was set equal to the A4 object,
        A2.prodAll();		//giving it the same values because it refers to the same object.
        A3.prodAll();
        A4.prodAll();
        A5.prodAll();
        A1.printProdAll();
        A2.printProdAll();
        A3.printProdAll();
        A4.printProdAll(); //why identical results here and from next line
        A5.printProdAll(); //Just like before, when the object A5 was created
    }					   //instead of allocating new space in the memory for
}    					   //it, it was set equal to the A4 object, giving it the same values
						   //because it refers to the same object Therefore, when the A5.prodAll()
						   //method was used, the resulting values are the same as when the A4.prodAll() 
						   //method was used.