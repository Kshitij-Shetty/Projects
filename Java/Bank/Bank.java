import java.io.*;
import java.lang.*;

class Bank
{
	BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	void create_Acc()throws IOException
	{
		FileWriter fw= new FileWriter("acc.txt",true);
	        BufferedWriter bw= new BufferedWriter(fw);
        	bw.close();
        	FileWriter fw10= new FileWriter("k.txt",true);
	        BufferedWriter bw10= new BufferedWriter(fw10);
        	bw10.close();
        	BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        	FileReader fr= new FileReader("acc.txt");
        	FileReader fr1= new FileReader("k.txt");
        	int i,j=0;
        	String a,f,k;
        	i=(fr.read())% 48;
        	if(i==-1)
        	{
        		i=0;
           		System.out.println("The account number allotted to you is 110"+j+(i+1)+".\n");
           		FileWriter fw7= new FileWriter("acc.txt");
           		BufferedWriter bw7= new BufferedWriter(fw7);
         		bw7.write(i);
           		bw7.close();
        	}
        	else if(i==9)
        	{
            		j=(fr1.read())% 48;
            		if(j==-1)
           		{
                		j=0;
            		}
           		System.out.println("The account number allotted to you is 110"+(j+1)+0+".\n");
           		FileWriter fw8= new FileWriter("acc.txt");
           		BufferedWriter bw8= new BufferedWriter(fw8);
           		bw8.write(0);
           		bw8.close();
           		FileWriter fw11= new FileWriter("k.txt");
           		BufferedWriter bw11= new BufferedWriter(fw11);
           		bw11.write(j+1);
           		bw11.close();
        	}
        	else
        	{   
        		j=(fr1.read())% 48;
            		if(j==-1)
            		{
                		j=0;
           	 	}
            		System.out.println("The account number allotted to you is 110"+j+(i+2)+".\n");
            		FileWriter fw9= new FileWriter("acc.txt");
            		BufferedWriter bw9= new BufferedWriter(fw9);
           		bw9.write(i+1);
            		bw9.close();
        	}
        	System.out.println("Enter a password for your account.\n");
        	a=br.readLine();
        	FileWriter fw2= new FileWriter("110"+j+(i+1)+a+".txt",true);
        	BufferedWriter bw2= new BufferedWriter(fw2);
                FileWriter fw20= new FileWriter("110"+j+(i+1)+a+"b.txt");
                BufferedWriter bw20= new BufferedWriter(fw20);
        	System.out.print("Enter your initial deposit.\n");
                
        	k=br.readLine();
                bw20.write(k);
                bw20.close();
        	bw2.write("Your initial deposit is Rupees "+k+".\n");
        	bw2.close();
        	System.out.println("Log into your account to perform further transactions.\n");
    	}
    	void login()throws IOException
    	{
    		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        	int i,j,g,k,bal;
        	String a,f;
        	System.out.println("Welcome.\n This is the login portal.\n");
        	for(g=0;g==0;)
        	{
        		g++;
            		System.out.println("Please enter your account number.\n");
            		i=Integer.parseInt(br.readLine());
            		System.out.println("Please enter your password.\n");
            		a=br.readLine();
            		FileWriter fw= new FileWriter(i+a+".txt",true);
            		BufferedWriter bw= new BufferedWriter(fw);
            		FileReader fr= new FileReader(i+a+".txt");
            		if((fr.read())==-1)
            		{
                		System.out.println("The combination of account number and password is incorrect.\nPlease try again.\n");
                		g=0;
            		}
            		else
            		{
                		System.out.println("You have logged in successfully.\n");
                		f=(i+a);
                                bal=balance(f);
                                System.out.println("Your Current Balance is "+bal+".\n");
        			//System.out.println(f+"\n");
                		for(j=0;(j!=1)&&(j!=2)&&(j!=3)&&(j!=4);)
                		{
                    			System.out.println("Enter:\n1 to deposit. \n2 to withdraw.\n3 to view previous transactions. \n4 to log out.\n");
                    			j=Integer.parseInt(br.readLine());
                    			if(j==1)
                    			{
                        			deposit(f);
                    			}
                    			else if(j==2)
                    			{
                        			withdraw(f);
                    			}
                    			else if(j==3)
                    			{
                        			transactions(f);
                    			}
                    			else if(j==4)
                    			{
                    			}
                    			else
                    			{
                        			System.out.println("Wrong input.\n Try again. \n");
                    			}
                		}
            		}
		}
	}
	void deposit(String f)throws IOException
    	{
    		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    		int i,j,k,bal;
    		String m;
                bal=balance(f);
    		FileWriter fw= new FileWriter(f+".txt",true);
            	BufferedWriter bw= new BufferedWriter(fw);
    		System.out.println("Enter the amount you want to deposit.\n");
                k=Integer.parseInt(br.readLine());
                bal=bal+k;
                m=Integer.toString(bal);
                System.out.println("Your Current Balance is Rupees "+m+".\n");
                bw.write("You have deposited Rupees "+k+".\n Your Current Balance is Rupees "+m+".\n");
                bw.close();
                FileWriter fw20= new FileWriter(f+"b.txt");
                BufferedWriter bw20= new BufferedWriter(fw20);
                bw20.write(m);
                bw20.close();
                for(j=0;(j!=1)&&(j!=2)&&(j!=3)&&(j!=4);)
                {
                    	System.out.println("Enter:\n1 to deposit.\n2 to withdraw.\n3 to view previous transactions.\n4 to log out.\n");
                    	j=Integer.parseInt(br.readLine());
                    	if(j==1)
                    	{
                        	deposit(f);
                    	}
                    	else if(j==2)
                    	{
                        	withdraw(f);
                    	}
                    	else if(j==3)
                    	{
                        	transactions(f);
                    	}
                    	else if(j==4)
                    	{
                    	}
                    	else
                    	{
                        	System.out.println("Wrong input.\n Try again. \n");
                    	}
                }    
    	}
    	void withdraw(String f)throws IOException
    	{
    		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    		int i,j,k,bal,a;
    		String m;
    		FileWriter fw= new FileWriter(f+".txt",true);
            	BufferedWriter bw= new BufferedWriter(fw);
                bal=balance(f);
                for(a=0;a==0;)
                {
                	a++;
    			System.out.println("Enter the amount you want to withdraw.\n");
                	k=Integer.parseInt(br.readLine());
                	if(k>bal)
                	{
                    		System.out.println("Your Amount You want to Withdraw is Greater than Your Balance.\nPlease Try Again\n");
                    		a=0;
                	}
                	else
                	{
                		bal=bal-k;  
                		m=Integer.toString(bal);  
                		System.out.println("Your Current Balance is Rupees "+m+".\n");
                		bw.write("You have withdrawn Rupees "+k+".\nYour Current Balance is Rupees "+m+".\n");
                		bw.close();
                		FileWriter fw20= new FileWriter(f+"b.txt");
                		BufferedWriter bw20= new BufferedWriter(fw20);
                		bw20.write(m);
                		bw20.close();
                		for(j=0;(j!=1)&&(j!=2)&&(j!=3)&&(j!=4);)
                		{
                    			System.out.println("Enter:\n1 to deposit. \n2 to withdraw.\n3 to view previous transactions. \n4 to log out.\n");	
                    			j=Integer.parseInt(br.readLine());
                    			if(j==1)
                    			{
                        			deposit(f);
                    			}
                    			else if(j==2)
                    			{
                        			withdraw(f);
                    			}
                    			else if(j==3)
                    			{
                        			transactions(f);
                    	}
                    	else if(j==4)
                    	{
                    	}
                    	else
                    	{
                        	System.out.println("Wrong input.\n Try again. \n");
                    	}
                }
                } 
                }
    	}
    	void transactions(String f)throws IOException
    	{
    		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    		int i,j,k;
    		char [] c=new char[1000];
    		FileReader fr= new FileReader(f+".txt");
    		fr.read(c);
                System.out.println("Your past transactions are as follows:\n\n");
                System.out.println(c);
                /*FileWriter fw15= new FileWriter("abc.txt");
	        BufferedWriter bw15= new BufferedWriter(fw15);
	        bw15.write(c);
        	bw15.close();*/
        	for(j=0;(j!=1)&&(j!=2)&&(j!=3)&&(j!=4);)
                {
                    	System.out.println("Enter:\n1 to deposit. \n2 to withdraw.\n3 to view previous transactions. \n4 to log out.\n");
                    	j=Integer.parseInt(br.readLine());
                    	if(j==1)
                    	{
                        	deposit(f);
                    	}
                    	else if(j==2)
                    	{
                        	withdraw(f);
                    	}
                    	else if(j==3)
                    	{
                        	transactions(f);
                    	}
                    	else if(j==4)
                    	{
                    	}
                    	else
                    	{
                        	System.out.println("Wrong input.\n Try again. \n");
                    	}
                }
        }
        
        int balance(String f)throws IOException
        {
            int x=0,y=0,z=0,i,count=0;
            //String a;
            char b []=new char[100];
            
            FileReader fr1= new FileReader(f+"b.txt");
            fr1.read(b);
            //System.out.println("b="+b);
            String a= new String(b);
            //System.out.println("a="+a);
            
            for(i=0;b[i]!='\0';i++)
            {
                count++;
            }
            //System.out.println(i);
            for(z=0;z<i;z++)
                {
                   y=a.charAt(z)-'0';
                   x=x*10+y;
                }
            return(x);
            
        }
    	public static void main(String args[])throws IOException
    	{
   		System.out.println("Welcome to St. John's Students Bank.\n\n");
        	Bank b= new Bank();
        	FileWriter fw= new FileWriter("acc.txt",true);
        	BufferedWriter bw= new BufferedWriter(fw);
        	BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        	FileReader fr= new FileReader("acc.txt");
        	int i,j,a;
        	if((j=fr.read())==-1)
        	{
            		for(j=0;(j!=1)&&(j!=2);)
            		{
                		System.out.println("Currently our bank doesn't have any accounts.\nWould you like to create one?\nSelect:\n1 to create a new account.\n2 to exit.\n");
                		j=Integer.parseInt(br.readLine());
                		if(j==1)
                		{
                    			b.create_Acc();
                    			j=1;
                		}
                		else if(j==2)
                		{
                			System.out.println("Thank you!\n Come again. \n");
                		}
                		else
               	 		{
                   	 		System.out.println("Wrong input.\n Try again. \n");
				}
                	}
            	}
        	for(j=0;(j!=1)&&(j!=2)&&(j!=3);)
        	{
        		System.out.println("Press:\n1 to login to your account.\n2 to create a new account. \n3 to exit.\n");
        	        j=Integer.parseInt(br.readLine());
        	        if(j==1)
        	        {
        	            b.login();
        	        }
        	        else if(j==2)
        	        {
        	            b.create_Acc();
        	        }
        	        else if(j==3)
        	        {
        	        	System.out.println("Thank you!\n Come again. \n");
        	        }
        	        else
        	        {
        	            System.out.println("Wrong input.\n Try again. \n");
        	        }
		}
	}
}    
