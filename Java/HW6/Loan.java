package HW6;

	import java.util.Random;

	/*Loan class serves as a part of Bank class to maintain loan information and to calculate monthly installments and total paid amount*/
	public class Loan 
	{
	    private double annualInterestRate;
	    private int numberOfYears;
	    private double loanAmount;
	    private java.util.Date loanDate;
	    
	    /* Default constructor */
	    public Loan() 
	    {
	        Random ranValue = new Random();
	        this.annualInterestRate = ranValue.nextInt(1,1000)/100.0;
	        loanDate = new java.util.Date();   
	    }
	    
	    /* Construct a loan with specified annual interest rate,number of years, and loan amount */
	    public Loan(double annualInterestRate, int numberOfYears,double loanAmount) 
	    {
	        this.annualInterestRate = annualInterestRate;
	        this.numberOfYears = numberOfYears;
	        this.loanAmount = loanAmount;
	        loanDate = new java.util.Date();
	    }

	    /* Return annualInterestRate */
	    public double getAnnualInterestRate() 
	    {
	        return annualInterestRate;
	    }

	    /* Set a new annualInterestRate */
	    public void setAnnualInterestRate(double annualInterestRate) 
	    {
	        this.annualInterestRate = annualInterestRate;
	    }

	    /* Return numberOfYears */
	    public int getNumberOfYears() {
	        return numberOfYears;
	    }

	    /* Set a new numberOfYears */
	    public void setNumberOfYears(int numberOfYears) {
	        this.numberOfYears = numberOfYears;
	    }
	    
	    /* Return loanAmount */
	    public double getLoanAmount() {
	        return loanAmount;
	    }

	    /* Set a new loanAmount */
	    public void setLoanAmount(double loanAmount) {
	            this.loanAmount = loanAmount;
	    }

	    /* Find monthly payment */
	    public double getMonthlyPayment() {
	        double monthlyInterestRate = annualInterestRate / 1200;
	        double monthlyPayment = loanAmount * monthlyInterestRate / (1 -(1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12)));
	        return monthlyPayment;
	    }
	    
	    
	    /* Find total payment */
	    public double getTotalPayment() {
	        double totalPayment = getMonthlyPayment() * numberOfYears * 12;
	        return totalPayment;
	    }

	    /* Return loan date */
	    public java.util.Date getLoanDate() {
	        return loanDate;
	    }

	    /* Set a new loan date */
	    public void setLoanDate(java.util.Date loanDate) {
	        this.loanDate = loanDate;
	    }
	 }