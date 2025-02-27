package HW1;
import java.util.Scanner; //for keyboard input
import java.util.Random; //to generate random numbers

public class Exp4
{
  public static void main(String[] args)
  {
   Scanner read = new Scanner(System.in);

   while(true)
   {
    System.out.print("Menu\n"+ "Press 1 to solve linear equations\n"+ 
    		"Press 2 to calcuate the shopping bill\n"+ "Press 3 for directions\n"+ 
    		"Press 4 for square root and cube root of n numbers\n"+"Press 5 to "+
    		"quit\n Enter the number of the task you want to perform: ");

    int choice = read.nextInt();

    if(choice == 1)
    {
     //invoke the method that performs the task 1
     task1();
    }
    else if(choice ==2)
    {
     //invoke the method that performs task 2
     task2();
    }
    else if(choice == 3)
    {
    //invoke the method that performs task 3
     task3();
    }
    else if(choice == 4)
    {
    //invoke the method that performs task 4
     task4();
    }
    else if(choice == 5)
    {
    //invoke the method that performs the quit task
     quit();
    }
    else
    {
    //invoke the method that displays the error message
     errorMssg();
    }
   }
 }

  public static void errorMssg()
  {
   System.out.println("\nINVALID CHOICE...Try again...!!!!\n");
  }

  public static void quit()
  {
   System.out.println("\nBye...Thank you for using this application...");
   System.exit(0); //Exits the program
  }

  public static void task1()
  {
   //logic: Write code to perform subtask
   System.out.println("\nTask1 execution");
   Scanner read = new Scanner(System.in);
   
   System.out.println("Enter values for your two linear equations in the format "
		   +"ax+by=e and cx+dy=f to solve for x and y");
   //Ask user for all the values
   System.out.print("Enter your value for a: ");
   float a = read.nextFloat();
   System.out.print("Enter your value for b: ");
   float b = read.nextFloat();
   System.out.print("Enter your value for e: ");
   float e = read.nextFloat();
   System.out.print("Enter your value for c: ");
   float c = read.nextFloat();
   System.out.print("Enter your value for d: ");
   float d = read.nextFloat();
   System.out.print("Enter your value for f: ");
   float f = read.nextFloat();
   
   //Calculate x and y using the formula
   double x = ((e*d)-(b*f)) / ((a*d)-(b*c));
   double y = ((a*f)-(e*c)) / ((a*d)-(b*c));
   System.out.println("The value of x is: "+x+"\n"+"The value of y is: "+y+"\n");
  }

  public static void task2()
  {
   //logic: Write code to perform subtask
   System.out.println("\nTask2 execution");
   Scanner read = new Scanner(System.in);
   
   //Declare and initialize items and their costs
   final double MONITOR = 100.0, KEYBOARD = 50.0, MOUSE = 35.0, CPU = 500, 
		   RAM = 400.0, SSD = 200.0, TAX = 7.2;
   
   System.out.println("A monitor costs $100.00, a keyboard costs $50.00, a mouse"
		   +" costs $35.00, a CPU costs $500.00, RAM costs $400.00, a SSD costs"
		   + " $200.00, and the sales tax is 7.2%.");
   System.out.println("Please enter the amount of each item you want to buy: ");
   
   //Ask user for the amount of each item
   System.out.print("Monitor: ");
   int monitorAmount = read.nextInt();
   System.out.print("Keyboard: ");
   int keyboardAmount = read.nextInt();
   System.out.print("Mouse: ");
   int mouseAmount = read.nextInt();
   System.out.print("CPU: ");
   int CPU_Amount = read.nextInt();
   System.out.print("RAM: ");
   int RAM_Amount = read.nextInt();
   System.out.print("SSD: ");
   int SSD_Amount = read.nextInt();
   
   //Calculate the cost of all the items purchased
   double cost = ((MONITOR*monitorAmount)+(KEYBOARD*keyboardAmount)+
		   (MOUSE*mouseAmount)+(CPU*CPU_Amount)+(RAM*RAM_Amount)+
		   (SSD*SSD_Amount));
   double totalTax = cost*(TAX/100); //Calculate the total sales tax
   double total = cost + totalTax; //Calculate the total cost overall
   System.out.println("The shopping bill total is: $"+total+"\n");
  }
  
  public static void task3()
  {
   //logic: Write code to perform subtask
   System.out.println("\nTask3 execution");
   Random gen = new Random();//creates object gen of type Random
   
   int sum = 0; //declare a counting variable with a starting value of 0
   while (sum <= 1000) //stop when the total of all the generated number is 
   //greater than 1000
   {
	   int number = gen.nextInt(10, 100);

	   if (number == 50)
	   {
		   System.out.println("RIGHT TURN");
	   }
	   else if (number == 60)
	   {
		   System.out.println("LEFT TURN");
	   }
	   else
	   {
		   System.out.println("STRAIGHT");
	   }
	   sum += number; //Add the generated number to the counting variable each time
   }
   System.out.println();
  }
  
  public static void task4()
  {
   //logic: Write code to perform subtask
   System.out.println("\nTask4 execution");
   Scanner read = new Scanner(System.in);
   
   System.out.println("How many numbers do you want to calculate the square root "
   		+ "and cubed root of?");
   int amount = read.nextInt(); //for the amount of number calculated
   
   System.out.println("Number  Sqrt    Cbrt"); //table heading
   System.out.println("--------------------");
   for (int i = 0; i <= amount; i++) //execute the correct number of times
   {
	   System.out.println(i+" \t"+String.format("%.2f",Math.sqrt(i))+" \t"+
			String.format("%.2f",Math.cbrt(i))); //display sqrt and cbrt to 2 
	   //decimal places
   }
   System.out.println();
  }
}