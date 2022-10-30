import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="r00t",
    host="localhost",
    database="fynd",
)

cur = con.cursor()


# input function to process inputs given by the user
def search(roll, mailch):

    cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [roll])

    studata = [i for i in cur]
    if len(studata) == 0:
        print("data not found")
    else:
        for i in studata:
            print(i)
    print(f"{studata[0][5]} {studata[0][4]}")
    # con.close()

# if input is 'y' or 'Y', then the user wants the email to be sent
    if mailch == 'y' or mailch == 'Y':

        stuname = studata[0][2]
        roll = studata[0][1]
        dob = studata[0][8]
        age = studata[0][7]
        gender = studata[0][3]
        residence = f"{studata[0][5]} {studata[0][4]}"
        lecs = studata[0][10]
        emailid = studata[0][9]

        # making a report pdf by taking some data from above
        from genreport import genpdf
        genpdf(stuname, roll, dob, age, gender, residence, lecs)

        # sends the pdf file to the specified email id of the candidate
        from mailto import sendmail
        sendmail(emailid, stuname)


if __name__ == "__main__":
    search(2, 'y')

