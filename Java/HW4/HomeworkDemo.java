package HW4;

public class HomeworkDemo
{
	public static void main(String args[])
	{
		//1st Person object: Uses the zero-parameterized constructor, demonstrates the 
		//checkVotingEligibilty method within the readObjectFields method, demonstrates the
		//readObjectFields method within the zero-parameterized constructor, and demonstrates
		//the display method within the main method of this class
		Person Bob = new Person();
		System.out.println("\n1st person object (Using Zero-parameterized Constructor): ");
		Bob.display();
		
		//2nd Person object: Uses the five-parameterized constructor, demonstrates the 
		//checkVotingEligibilty method within the five-parameterized constructor, and demonstrates
		//the display method within the main method of this class
		Person Sarah = new Person("Sarah Roberts", 23, "Janitor", "123 Tarleton", 'F');
		System.out.println("\n2nd person object (Using Five-parameterized Constructor: ");
		Sarah.display();
		
		//3rd Person object: Uses the copy constructor and demonstrates the display method
		//within the main method of this class
		Person Sarah2 = new Person(Sarah);
		System.out.println("\n3rd person object (Using Copy Constructor): ");
		Sarah2.display();
		
		//1st Television object: Uses a zero-paramterized constructor
		System.out.println("\n1st Televison object (Using Zero-parameterized Constructor): ");
		Television TV1 = new Television();
		TV1.display();
		
		//2nd Television object: Uses a three-paramterized constructor
		System.out.println("\n2nd Televison object (Using Three-parameterized Constructor): ");
		Television TV2 = new Television(99,5,false);
		TV2.display();
		
		//3rd Television object: Uses a copy constructor
		System.out.println("\n3rd Televison object (Using Copy Constructor): ");
		Television TV3 = new Television(TV2);
		TV3.display();
		
		//Demonstrate all methods of the Television class
		System.out.println();
		TV3.turnOn();
		System.out.println("\n3rd Televison object after turnOn method:");
		TV3.display();
		TV3.turnOff();
		System.out.println("\n3rd Televison object after turnOff method:");
		TV3.display();
		TV3.setChannel(101);
		TV3.setVolume(2);
		System.out.println("\n3rd Televison object after setChannel and setVolume methods:");
		TV3.display();
		TV3.channelUp();
		System.out.println("\n3rd Televison object after channelUp method:");
		TV3.display();
		TV3.channelDown();
		System.out.println("\n3rd Televison object after channelDown method:");
		TV3.display();
		TV3.volumeUp();
		System.out.println("\n3rd Televison object after volumeUp method:");
		TV3.display();
		TV3.volumeDown();
		System.out.println("\n3rd Televison object after volumeDown method:");
		TV3.display();
	}
}