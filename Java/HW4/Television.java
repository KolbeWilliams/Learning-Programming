package HW4;
import java.util.Scanner;

public class Television
{
	//Instance Variables
	private int channel = 1;
	private int volume = 1;
	private Boolean on = false;
	
	//Constructors
	public Television()
	{
		//read for all fields
		String state = null;
		Scanner read = new Scanner(System.in);
		do
		{
			System.out.print("Enter the channel (1-120): ");
			channel = read.nextInt();
			if(channel < 1 || channel > 120)
				System.out.println("Please enter a channel from 1-120");
		}while(channel < 1 || channel > 120);
		do
		{
			System.out.print("Enter the volume level (1-7): ");
			volume = read.nextInt();
			if(volume < 1 || volume > 7)
				System.out.println("Please enter a volume level from 1-7");
		}while(volume < 1 || volume > 7);
		read.nextLine();
		do
		{
			System.out.print("Indicate if the Televison is on/off: ");
			state = read.nextLine();
			if("on".equals(state))
				on = true;
			else if("off".equals(state))
				on = false;
			if(!"on".equals(state) && !"off".equals(state))
					System.out.println("Please enter either \"on\" or \"off\"");
		}while(!"on".equals(state) && !"off".equals(state));
	}
	
	public Television(int channel, int volume, Boolean on)
	{
		//Set all values for object
		this.channel = channel;
		this.volume = volume;
		this.on = on;
	}
	
	Television(Television copy)
	{
		//Set all values for object
		this.channel = copy.channel;
		this.volume = copy.volume;
		this.on = copy.on;
	}
	
	//Methods
	void turnOn()
	{
		this.on = true;
	}
	
	void turnOff()
	{
		this.on = false;
	}
	
	void setChannel(int newChannel)
	{
		this.channel = newChannel;
	}
	
	void setVolume(int newVolumeLevel)
	{
		this.volume = newVolumeLevel;
	}
	
	void channelUp()
	{
		this.channel++;
	}
	
	void channelDown()
	{
		this.channel--;
	}
	
	void volumeUp()
	{
		this.volume++;
	}
	
	void volumeDown()
	{
		this.volume--;
	}
	
	void display()
	{
		System.out.print("Channel: "+ this.channel + "\nVolume: " + this.volume + "\nOn/Off: ");
		if(this.on == true)
			System.out.print("On\n");
		else
			System.out.print("Off\n");
	}
}