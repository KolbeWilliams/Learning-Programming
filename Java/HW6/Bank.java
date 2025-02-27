package HW6;

import java.util.Random;
import java.util.Scanner;

/*Bank class maintains banks information.*/
public class Bank 
{
    private String bankName;
    private int bankCode;
    Loan loanInfo;  
    
    /* constructor to create initial banks with names, codes, and loan information with annualInterestRate, and quote created date*/
    Bank()
    {
        Random ranValue = new Random();
        String bankNames[] = {"Wells Fargo","City Bank","Chase","Discovery","Terra Bank","PNC Financial Services","Capital One Financial"};
        this.setBankName(bankNames[ranValue.nextInt(bankNames.length)]);
        this.bankCode = 1+ranValue.nextInt(99);
        //System.out.println(this.bankCode);
        loanInfo = new Loan();
    }
    
    
    
    /* constructor to create each matched banks with bank's names, bank's codes, 
     * and bank's loan information with bank's annualInterestRate, quote created date, user specified numbeOfYears, user specified loanAmount 
     * and prints the matched bank's bank name, bank code, AnnualInterestRate, loan amount, monthly payment, numberOfMonths, total payment, quote created date*/
    Bank(Bank bank, double annualInterestRate, int numberOfYears, double loanAmount, BankFinder c)
    {
        /*write your code*/
    	if(bank.loanInfo.getAnnualInterestRate() <= annualInterestRate)
    	{
    		this.bankName = bank.bankName;
    		this.bankCode = bank.bankCode;
    		this.loanInfo = bank.loanInfo;
    		this.loanInfo.setAnnualInterestRate(bank.loanInfo.getAnnualInterestRate());
    		this.loanInfo.setNumberOfYears(numberOfYears);
    		this.loanInfo.setLoanAmount(loanAmount);
    		System.out.printf("|%-30s%10d%20.2f%20.2f%20.2f%20d%20.2f%30s|\n",this.getBankName(),this.getBankCode(),
    				this.loanInfo.getAnnualInterestRate(),loanAmount,this.loanInfo.getMonthlyPayment(),
    				this.loanInfo.getNumberOfYears() * 12,this.loanInfo.getTotalPayment(),this.loanInfo.getLoanDate());
    		c.count++;
    	}
    }
    
    
    /*returns the total banks need to be checked*/
    public static int howMany()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("With how many banks you want to check: ");
        return input.nextInt();
    }
    
    
    /*prints all banks with bank name, bank codes, bank annualInteresrtRate, and quote created date */
    public static void printBanksCodes(Bank banks[])
    {
        /*write your code*/
    	for(int i=1;i<173;i++)
            System.out.print("_");
        System.out.printf("\n|%-30s%10s%20s%30s|\n","Banks","Codes","AnnualInterestRate","Date");
        for(int i = 0; i < banks.length; i++)
    	{
        	System.out.printf("|%-30s%10d%20.2f%30s|\n", banks[i].getBankName(), banks[i].getBankCode(), banks[i].loanInfo.getAnnualInterestRate(),
        			banks[i].loanInfo.getLoanDate());
    	}
        for(int i=1;i<175-2;i++)
            System.out.print("_");
        System.out.println();
    }
    
    /*returns bankName */
    public String getBankName() {
        return bankName;
    }
    
    /*sets a new bankName*/
    public void setBankName(String bankName) {
        this.bankName = bankName;
    }
    
    /*returns bankCode */
    public int getBankCode() {
        return bankCode;
    }
    
    /*sets a new bankCode*/
    public void setBankCode(int bankCode) {
        this.bankCode = bankCode;
    }

    /*returns loanInfo */
    public Loan getLoanInfo() {
        return loanInfo;
    }
    
    /*sets a new loanInfo*/
    public void setLoanInfo(Loan loanInfo) {
        this.loanInfo = loanInfo;
    }
}