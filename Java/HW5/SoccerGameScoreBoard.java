package HW5;
import java.util.Scanner;

public class SoccerGameScoreBoard 
{
	String sTeamName;
    int goalsInMatch;
    int goalsInExtraTime;
    int goalsInPenaltyShootOut;
    static int countTeams;
    
    static 
    {
    	countTeams = 0;
    }
    
    /*include constructor chaining so that you can create an object with only the team name, later
     * in chaining, you can use a read method to read the rest of the field value
     * hint: while calling the next constructor, you can place a call to read function as
     * argument in the constructor call
     */
    
    SoccerGameScoreBoard(String sTeamName)
    {
    	//calls the read method to return three integers and calls the next constructor in the chain
    	this(readMeth("Enter the goals socred in the match by " + sTeamName + ": "), 
    			readMeth("Enter the goals socred in extra time by " + sTeamName + ": "),
    			readMeth("Enter the goals socred in the penalty shoot out by " + sTeamName + ": ")); 
    	this.sTeamName = sTeamName;
    	countTeams++; //increase countTeams variable when object is created
    }
    
    //the final constructor in the chain initializes all of the instance variables for the invoking object
    SoccerGameScoreBoard(int num1, int num2, int num3)
    {
    	this.goalsInMatch = num1;
    	this.goalsInExtraTime = num2;
    	this.goalsInPenaltyShootOut = num3;
    }

    SoccerGameScoreBoard(String sTeamName, int goalsInMatch, int goalsInExtraTime, int goalsInPenaltyShootOut)
    {
          this.sTeamName = sTeamName;
          this.goalsInMatch = goalsInMatch;
          this.goalsInExtraTime = goalsInExtraTime;
          this.goalsInPenaltyShootOut = goalsInPenaltyShootOut;
          countTeams++; //increase countTeams variable when object is created
    }
    
    //read method reads an integer
    public static int readMeth(String msg)
    {
    	Scanner read = new Scanner(System.in);
    	System.out.print(msg);
    	return read.nextInt();
    }
    
    @Override
    public String toString() {
          return "SoccerGameScoreBoard [sTeamName=" + sTeamName + ", goalsInMatch=" + goalsInMatch + ", goalsInExtraTime="
                        + goalsInExtraTime + ", goalsInPenaltyShootOut=" + goalsInPenaltyShootOut + "]";
    }
}
