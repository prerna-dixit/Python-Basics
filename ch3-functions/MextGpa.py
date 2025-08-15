#calculates gpa according to the mext scale/ 3.0 grading scale used in japanese universities

#"The GPA, or grade point average, is part of the criteria stated by MEXT for the scholarship applicants. Applicants must score GPA of 2.50 or above on a 
#3-point MEXT grading scale (average of courses registered in the most recent 1-year as full-time degree student) to be eligible to apply for the MEXT scholarship. 
# Using the MEXT-specified grade conversion chart and GPA calculation formula below, please check your eligibility. "	

#grade conversion chart
# Grading System	Grade				
#Type 1		         Excellent	Good	Average	Fail
#Type 2		           A	     B	      C	      F
#Type 3		        100-80	   79-70  	69-60	below 59
#Type 4	     S	     A	         B	      C	      F
#Type 5	     A	     B	         C	      D       F
#Type 6	  100-90	89-80	   79-70	69-60	below 59
#Grade Point 3	    3	        2	      1	      0

#GPA CALCULATION FORMULA
#  ([No. of GP3 Credits] x 3) + ([No. of GP2 Credits] x 2) + ([No. of GP1 Credits] x 1) + ([No. of GP0 Credits] x 0) /Total number of credits registered

#where GP = Grade Point

# MEXT GPA Calculator (3.0 scale)

def mextGPA():
    print("=== MEXT GPA Calculator ===")
    print("Enter the number of credits for each grade point:")

    try:
        gp3 = float(input("Credits with Grade Point 3 (Excellent): "))
        gp2 = float(input("Credits with Grade Point 2 (Good): "))
        gp1 = float(input("Credits with Grade Point 1 (Average): "))
        gp0 = float(input("Credits with Grade Point 0 (Fail): "))
    except ValueError:
        print("ERROR: Please enter valid numbers for credits.")
        return

    total_credits = gp3 + gp2 + gp1 + gp0
    if total_credits == 0:
        print("ERROR: Total credits cannot be zero.")
        return

    gpa = ((gp3 * 3) + (gp2 * 2) + (gp1 * 1) + (gp0 * 0)) / total_credits

    print(f"\nYour MEXT GPA is: {round(gpa, 2)}")
    if gpa >= 2.50:
        print("✅ Eligible to apply for the MEXT Scholarship.")
    else:
        print("❌ Not eligible to apply for the MEXT Scholarship.")

mextGPA()

								

													
														
														

														
