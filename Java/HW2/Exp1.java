package HW2;
import java.util.Scanner;

public class Exp1
{
	public static void main(String args[])
	{
		Scanner read = new Scanner(System.in);
		int D = read.nextInt();
		int N = read.nextInt();
		int trip = D*2; //Calculates the round trip distance
		int days = N; //Stores the number of days
		
		int Xa = read.nextInt(); //Reads input for Uber values
		int Xb = read.nextInt();
		int Xc = read.nextInt();
		int uber = (Xa+((trip-Xb)*Xc))*days; //Calculates Uber price
		
		int Ya = read.nextInt(); //Reads input for Lyft values
		int Yb = read.nextInt();
		int Yc = read.nextInt();
		int lyft = (Ya+((trip-Yb)*Yc))*days; //Calculates Lyft price
		
		int Za = read.nextInt(); //Reads input for Motor Bike
		int Zb = read.nextInt();
		int Zc = read.nextInt();
		int Zd = read.nextInt();
		int bike = (Za+((trip/Zd)*Zb)+(40*Zc))*days; //Calculates Motor Bike price
		
		if(uber < lyft && uber < bike) //The if else ladder determines which is cheaper or if multiple options are the cheapest
			System.out.println("Uber is cheaper");
		else if(lyft < uber && lyft < bike)
			System.out.println("Lyft is cheaper");
		else if(bike < uber && bike < lyft)
			System.out.println("Renting a Motor Bike is cheaper");
		else if(uber == lyft && uber < bike)
			System.out.println("Uber is cheaper and Lyft is cheaper");
		else if(uber == bike && uber < lyft)
			System.out.println("Uber is cheaper and renting a Motor Bike is cheaper");
		else
			System.out.println("Lyft and renting a Motor Bike is cheaper than Uber");
	}
}