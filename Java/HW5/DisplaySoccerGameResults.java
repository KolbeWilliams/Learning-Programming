package HW5;

public class DisplaySoccerGameResults
{	
	public static void main(String[] args)
	{
		SoccerGameScoreBoard machesterUnited = new SoccerGameScoreBoard("Machester United",3,1,5);
        SoccerGameScoreBoard liverpool = new SoccerGameScoreBoard("Liverpool",3,1,4);
        SoccerGameResults results = grabGameResults(machesterUnited,liverpool);
        
        if(results.wonByGoalsInMatch)
        {
        	System.out.println(results.sWinnerTeam+" vs "+results.sLoserTeam+" and the winner is "+results.sWinnerTeam);
        }
        else if (results.wonBYGoalsInExtraTime)
        {
        	System.out.println(results.sWinnerTeam+" vs "+results.sLoserTeam+" and the winner is "+results.sWinnerTeam+" in Extra Time");
        }
        else if (results.wonByGoalsInPenaltyShootOut)
        {
        	System.out.println(results.sWinnerTeam+" vs "+results.sLoserTeam+" and the winner is "+results.sWinnerTeam+" in Penalty Shootout");
        }
        else
        {
        	System.out.println(results.sWinnerTeam+" vs "+results.sLoserTeam+" and they ended with a tie");
        }  
        
        /*create two more teams by using constructor chaining and display the result in the same way as did with liverpool and machesterUnited*/
        SoccerGameScoreBoard Argentina = new SoccerGameScoreBoard("Argintina");
        SoccerGameScoreBoard Brazil = new SoccerGameScoreBoard("Brazil");
        SoccerGameResults results2 = grabGameResults(Argentina,Brazil);
        
        //calculate who won and during what part of the game
        if(results2.wonByGoalsInMatch)
        {
        	System.out.println(results2.sWinnerTeam+" vs "+results2.sLoserTeam+" and the winner is "+results2.sWinnerTeam);
        }
        else if (results2.wonBYGoalsInExtraTime)
        {
        	System.out.println(results2.sWinnerTeam+" vs "+results2.sLoserTeam+" and the winner is "+results2.sWinnerTeam+" in Extra Time");
        }
        else if (results2.wonByGoalsInPenaltyShootOut)
        {
        	System.out.println(results2.sWinnerTeam+" vs "+results2.sLoserTeam+" and the winner is "+results2.sWinnerTeam+" in Penalty Shootout");
        }
        else
        {
        	System.out.println(results2.sWinnerTeam+" vs "+results2.sLoserTeam+" and they ended with a tie");
        }
      //display number of teams and scores for all teams
        System.out.println("\n" + SoccerGameScoreBoard.countTeams + " Teams were created:");
        System.out.println(machesterUnited.toString());
        System.out.println(liverpool.toString());
        System.out.println(Argentina.toString());
        System.out.println(Brazil.toString());
	}
	
	public static SoccerGameResults grabGameResults(SoccerGameScoreBoard team1,SoccerGameScoreBoard team2)
	{
        /*write your code to return the results*/
		SoccerGameResults temp = new SoccerGameResults(); //create a temporary object to hold the values so that it can be returned
		
		//use if else ladder to initialize the instance variables of the SoccerGameResults class
		if(team1.goalsInMatch < team2.goalsInMatch)
		{
			temp.sWinnerTeam = team2.sTeamName;
			temp.sLoserTeam = team1.sTeamName; 
			temp.wonByGoalsInMatch = true;
			temp.wonBYGoalsInExtraTime = temp.wonByGoalsInPenaltyShootOut = temp.DrawByTie = false;
		}
		else if(team1.goalsInMatch > team2.goalsInMatch)
		{
			temp.sWinnerTeam = team1.sTeamName;
			temp.sLoserTeam = team2.sTeamName; 
			temp.wonByGoalsInMatch = true;
			temp.wonBYGoalsInExtraTime = temp.wonByGoalsInPenaltyShootOut = temp.DrawByTie = false;
		}
		else if(team1.goalsInExtraTime < team2.goalsInExtraTime)
		{
			temp.sWinnerTeam = team2.sTeamName;
			temp.sLoserTeam = team1.sTeamName; 
			temp.wonBYGoalsInExtraTime = true;
			temp.wonByGoalsInMatch = temp.wonByGoalsInPenaltyShootOut = temp.DrawByTie = false;
		}
		else if(team1.goalsInExtraTime > team2.goalsInExtraTime)
		{
			temp.sWinnerTeam = team1.sTeamName;
			temp.sLoserTeam = team2.sTeamName; 
			temp.wonBYGoalsInExtraTime = true;
			temp.wonByGoalsInMatch = temp.wonByGoalsInPenaltyShootOut = temp.DrawByTie = false;
		}
		else if(team1.goalsInPenaltyShootOut < team2.goalsInPenaltyShootOut)
		{
			temp.sWinnerTeam = team2.sTeamName;
			temp.sLoserTeam = team1.sTeamName;
			temp.wonByGoalsInPenaltyShootOut = true;
			temp.wonByGoalsInMatch = temp.wonBYGoalsInExtraTime = temp.DrawByTie = false;
		}
		else if(team1.goalsInPenaltyShootOut > team2.goalsInPenaltyShootOut)
		{
			temp.sWinnerTeam = team1.sTeamName;
			temp.sLoserTeam = team2.sTeamName;
			temp.wonByGoalsInPenaltyShootOut = true;
			temp.wonByGoalsInMatch = temp.wonBYGoalsInExtraTime = temp.DrawByTie = false;
		}
		else
		{
			temp.sWinnerTeam = team1.sTeamName;
			temp.sLoserTeam = team2.sTeamName;
			temp.DrawByTie = true;
			temp.wonByGoalsInMatch = temp.wonBYGoalsInExtraTime = temp.wonByGoalsInPenaltyShootOut = false;
		}
		return temp; //return the temporary object to the results object created
	}
}
