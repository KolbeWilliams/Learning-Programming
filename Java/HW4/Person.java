package HW4;
import java.util.Scanner;

public class Person
{
	
	//Instance Variables
	private String name = null;
	private int age = 1;
	private String occupation = null;
	private String address = null;
	private char gender = '\u0000';
	private Boolean eligibleToVote = false;
	
	//Constructors
	Person()
	{
		this.readObjectFields();
	}
	
	Person(String name, int age, String occupation, String address, char gender)
	{
		this.name = name;
		this.age = age;
		this.occupation = occupation;
		this.address = address;
		this.gender = gender;
		eligibleToVote = this.checkVotingEligibility();
	}
	
	Person(Person copy)
	{
		this.name = copy.name;
		this.age = copy.age;
		this.occupation = copy.occupation;
		this.address = copy.address;
		this.gender = copy.gender;
		eligibleToVote = copy.eligibleToVote;
	}
	
	//Methods
	boolean checkVotingEligibility()
	{
		if(this.age >= 18)
			return true;
		else
			return false;
	}
	
	void readObjectFields()
	{
		char gen = '\u0000';
		Scanner read = new Scanner(System.in);
		System.out.print("Enter the name of the person: ");
		name = read.nextLine();
		System.out.print("Enter the person's age: ");
		age = read.nextInt();
		read.nextLine();
		System.out.print("Enter the person's occupation: ");
		occupation = read.nextLine();
		System.out.print("Enter the person's address: ");
		address = read.nextLine();
		do
		{
			System.out.print("Enter the person's gender (use M or F): ");
			gen = read.next().charAt(0);
			if('M' == gen)
				gender = gen;
			else if('F' == gen)
				gender = gen;
			if('M' != gen && 'F' != gen)
					System.out.println("Please enter either capital \"M\" or capital \"F\"");
		}while('M' != gen && 'F' != gen);
		eligibleToVote = this.checkVotingEligibility();
	}
	
	void display()
	{
		System.out.print("Name: " + this.name + "\nAge: " + this.age + "\nOccupation: " 
				+ this.occupation + "\nAddress: " + this.address + "\nGender: " + this.gender
				+ "\nVoting Eligibility: ");
		if(this.eligibleToVote == true)
			System.out.print("Elgilible\n");
		else
			System.out.print("Not Eligible\n");
	}
}