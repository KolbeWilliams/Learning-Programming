package HW2;

public class Exp2

{
  public static void main(String[] args)
  {
   System.out.println("What is it printing?\nExplain the problem it is solving.");
   //The powers of two less than 1000 are printing because the testOne method is called in the if statement
   //Only numbers that are a power of two will return true from the testOne method and be printed.
   for(int i=1;i<1000;i++)
     if(testOne(i))
       System.out.println(i);
   
   System.out.println("What is it printing?\nExplain the problem it is solving.");
   //The number of binary 1s, or set bits, for each number in the for loop (1-19) are printed because the 
   //testTwo method is called in the for loop.
   //The number of set bits in a given number is returned from the testTwo method
   for(int i=1;i<20;i++)
       System.out.println(testTwo(i));
   
   System.out.println("What is it printing?\nExplain the problem it is solving.");
   //The unique subsets of the IHaveSomething array are printed because the testThree method is called, which 
   //returns all of the unique subsets.
   int[] iHaveSomething = new int[] { 22,33,44 };
   testThree(iHaveSomething);
  }

  //What is the purpose of this method?
  //The purpose is to determine if a given number is a power of two
  static boolean testOne(int hasSomething)
  {
   //Explain the following code with an example here
   //hasSomething != 0 ensures that 0 is not determined to be true, and the code after the && makes sure
   //that only powers of 2 return true using the & bitwise operator. The & bitwise operator compares the
   //binary values of the given number and the given number minus one. If all binary digits result in 0,
   //it is a power of two.
   ///For example, 16 in binary is 10000 and 16-1 in binary is 01111. When the & bitwise operator is used,
   //the resulting number is 00000 because none of the corresponding digits have a 1 in both binary numbers. 
   ///16 is a power of two, so it results in a value of 0. All powers of two will have this result.
   return hasSomething != 0 && ((hasSomething & (hasSomething - 1)) == 0);
  }

  //What is the purpose of this method?
  //The purpose of this method is to return the number of binary 1s, or set bits, for a given number.
  static int testTwo (int whoAmI)
  {
   int whatIamDoing=0;
   //What this loop is doing?
   //The while loop is counting the number of set bits by comparing the given number with the given number - 1
   //using the & bitwise operator and then assigning the result to the variable that originally held the given 
   //number (whoAmI). Each time this operation is performed, one set bit is removed from the number.
   //Then, the loop increments the set bit counter (whatIamDoing) until the variable reaches 0.
   while( whoAmI!=0 )
   {
       whoAmI = whoAmI&(whoAmI-1);
       whatIamDoing++;
   }
   //What is returned here to the caller?
   //The number of set bits is returned.
   return whatIamDoing;
  }

  //What is the purpose of this method?
  //The purpose of this method is to generate all the subsets of a given array.
  public static void testThree(int[] iHaveSomething)
  {
   int howMany = iHaveSomething.length;
   //How long does this loop run? Why this nested loop is implemented?
   //The amount of time the loop runs depends of the length of the given array. The << bitwise operator shifts
   //the binary bits of a number to the left. The operation effectively multiples the number by 2^the number 
   //after the <<. In this program, the given array has three elements, so 1 << howMany is the same as 1 << 3, 
   //which is equal to 1*2^3 = 8. Therefore, the loop runs from 0 to i < 8, which is a total of 8 times.
   //The nested for loop is implemented to check if each element should be included in the subset that is 
   //represented with the i variable in the first loop.
   for (int i = 0; i < (1 << howMany); i++)
   {
       for (int j = 0; j < howMany; j++)
       {
           //What actually is this if statement checking?
    //The if statement is checking if the number represented by i shares any set bits with the number 1
    //shifted left by the number represented by j. If it does share any set bits, the jth element in the ith
    //subset is printed. This works because all unique subsets will be printed.
           if ((i & (1 << j)) != 0)
           {
               System.out.print(iHaveSomething[j] + " ");
           }
       }
       System.out.println();
   }
  }
}