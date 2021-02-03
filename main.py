

citizen = input("Are you a U.S. citizen (or born in Puerto Rico, Guam, or U.S. Virgin Islands)? ")
if citizen[0].lower() == "n":
  print(" You are ineligible to vote in NY.")
if citizen[0].lower() == "y":
  age= input("Are you at least 18 years of age? ")
  if age[0].lower() =="n":
    print(" You are ineligible to vote in NY.")
  if age[0].lower() =="y":
    prison = input("Are you currently in prison or on parole for a felony conviction? ")
    if prison[0].lower() == "y":
      print(" You are ineligible to vote in NY.")
    if prison[0].lower() == "n":
      mental = input("Are you adjudged mentally incompetent by a court? ")
      if mental[0].lower() == "y":
        print(" You are ineligible to vote in NY.")
      if mental[0].lower() == "n":
        location = input("Will you vote or did you vote in another state? ")
        if location[0].lower() == "y":
          print(" You are ineligible to vote in NY.")
          citizen = "no"
        if location[0].lower() == "n":
          print(" You are eligible to vote in NY. ")
          moreinfo = input("Would you like to know more information on your local representatives? ")
          citizen = "yes"
          if moreinfo[0].lower() == "n":
            print(" Have a nice day!")


def rep_find(zipcode):
   if citizen == "yes":
    numbers = {
      "Yvette Clarke":[11203,11218,11210,11226,11212,11213,11215,11216,11217,11225,11226,11229,11230,11233,11234,11235,11236,11238],
      "Gregory Meeks":[11411,11412,11413,11419,11420,11422,11423,11429,11430],
      "Grace Meng":[11351,11355,11364,11365,11367,11374,11379,11415,11424,],
      "John Faso":[12015,12017,12017,12022,12024,12029,12031,12035,12036,12037,12040,12042,12043,12051,12052],
      "Nita Lowey":[10503,10510,10511,10514,10517,10520,10522,10523,10532,10533,10535,10545,10546,10547,10548]
     
      }
    for rep in numbers:
      if zipcode in numbers[rep]:
        return("Your local representative is "+rep)
      else:
        return("Your zipcode is not in our database. Feel free to use this alternative http://www.mygovnyc.org/") 
  

zipcode = int(input(" Please provide your zipcode ")) 
print(rep_find(zipcode))
      

#Code debugged by Tyler Robinson
#Code debugged by Nazmul Hoq
            
            
        
          
  

