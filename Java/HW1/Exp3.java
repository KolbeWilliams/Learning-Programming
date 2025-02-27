package HW1;

import java.security.cert.CertPathValidatorException.Reason;

class Exp3
{
    public static void main(String args[])
    {
        int a = 2147483647;
        byte b = 127;

        System.out.println(0B10111); //The output is 23 because 10111 is equal to 23
        // in binary and the 0B at the beginning of the number signifies that it is 
        //a binary number
        
        System.out.println(0345); //The output is 229 because 345 is equal to 229 in
        //base eight (octal), and the 0 at the beginning of the number signifies that it is
        //a number in octal.
        
        System.out.println(0xABCD); //The output is 43981 because ABCD is equal to
        //43981 in hexadecimal, and the 0x at the beginning of the number signifies
        //that it is a hexadecimal number
        
        System.out.println(1/3); //The output is 0 because 1/3 is equal to a decimal
        //less than 0.5, and 0 is the closest integer to the actual answer. The
        //output is an int since both 1 and 3 are ints.
        
        System.out.println(1/3.0); //The output is 0.3333333333333333 because that is
        //the value of 1/3 carried out to 16 decimal places, which is the maximum
        //amount a double can hold. Since 3.0 is a double value, JAVA automatically
        //casts 1 as a double value as well, which causes the output to be a double.
        
        System.out.println(1.0/3); //The output is the same as the last print 
        //statement for the same reason. The only difference is that 1.0 is a double 
        //and 3 is an int, so JAVA automatically casts 3 as a double.
        
        System.out.println(1.0f/3.0F); //The output is 0.33333334 because that is the
        //value of 1/3 carries out to 8 decimal places, which is the maximum amount a
        //float can hold. Since both 1.0f and 3.0f are float values (signified by the
        //f at the end of each one), the output is also a float value.
        
        
        System.out.println(123.123E-2); //The output is 1.23123 because the E-2 at
        //the end of the value represents scientific notation, and E-2 causes the
        //decimal to move left twice, resulting in 1.23123.
        
        System.out.println(a); //The output is 2147483647 because that is what the
        //variable a was initialized with in this program.
        
        System.out.println(b); //The output is 127 because that is what the variable
        //b was initialized with in this program.
        
        b = (byte) (b+1);
        System.out.println(b); //The output is -128 because b is a variable that has
        //a byte data type, which has a minimum value of -128 and a maximum value of
        //127. Since b was initialized with the maximum value that the a byte can
        //hold, adding 1 to it goes back to the minimum value, which is -128.
        
        a = (int) (a+1);
        System.out.println(a); //The output is -2147483648 because a is a variable
        //that has a int data type, which has a minimum value of -2147483647 and a
        //maximum value of 2147483647. Since a was initialized with the maximum value
        //that a int can hold, adding 1 to it goes back to the minimum value, which is
        //-2147483647.
        
        b = (byte) ((-b)+127);
        System.out.println(b); //The output is -1 because b is now equal to -128 +
        //127, which is equal to -1.
        
        a = (int) ((-a)+2147483647);
        System.out.println(a); //The output is -1 because a is now equal to
        //-2147483648 + 2147483647, which is equal to -1.
        
        a = 2147483647;
        b = 127;
        b = (byte) (b+1270);
        System.out.println(b); //The output is 117 because the minimum and maximum
        //values that the byte data type can hold are -128 and 127, and 127 + 1270
        //is 1397. 1397 goes from -128 to 127 5 times with 117 left over.
        
        a = (int) (a+2147483647);
        System.out.println(a); //The output is -2 because the minimum and maximum
        //values that the int data type can hold are -2147483648 and 2147483647, and
        //2147483647 + 2147483647 would start back at -2147483648 and reach -2.
    }
}