import pandas as pd
import requests
r = requests.get("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")
conferences = r.json()

## we can clearly see there are two types of confernces, which are Paid and Free
# function for all free conferences
def freeconferences():
    free  = conferences['free']
    for fre in free:
        print("-----------------------------------------------------------------------------")
        print(fre["confName"],",",fre["confStartDate"],",",fre["city"],",",fre["country"],",",fre["entryType"],",",fre["confUrl"])
    return None

#function for all paid
def paidconferences():
    paid  = conferences['paid']
    for pai in paid:
        print("-----------------------------------------------------------------------------")
        print(pai["confName"],",",pai["confStartDate"],",",pai["city"],",",pai["country"],",",pai["entryType"],",",pai["confUrl"])
    return None

# def all conferences
def all_conf():
    conf = conferences['free'] + conferences['paid']
    for allc in conf:
        print("-----------------------------------------------------------------------------")
        print(allc["confName"],",",allc["confStartDate"],",",allc["city"],",",allc["country"],",",allc["entryType"],",",allc["confUrl"])
    return None       

## semantic duplicate
def diffdict(dicta, dictb):
    count = 0
    for key in dicta.keys():
        if dicta[key] != dictb[key]:
        	count = count + 1
    return count

def semantic_duplicates(conferences):
	clones=[]
	for a in range(0,len(conferences)):
		for b in range(0,a):
			value = diffdict(conferences[a],conferences[b])
			if value<=3:
				clones.append(conferences[a])
	return clones
### storing all confernces in one file
allconf = conferences["paid"]+ conferences["free"]    
if __name__ == "__main__":
    while (True):
        print("#################")
        print("choose option")
        print("1) Free conferences")
        print("2) paid conferences")
        print("3) all conferences")
        print("4) semantic")
        print("5) create dataframe table")
        print("6) exit")
        print("#################")
        option = int(input())
        if option == 1:
            freeconferences()
        if option == 2:
            paidconferences()
        if option == 3:
            all_conf()
        if option == 4:
            x = semantic_duplicates(allconf)
            for y in x:
                print("--------")
                print(y["confName"],",",y["confStartDate"],",",y["city"],",",y["country"],",",y["entryType"],",",y["confUrl"])
                print("--------")
        if option == 5:
            emailIds = []
            city = []
            country = []
            imageUrl = []
            venue = []
            confName = []
            state = []
            confEndDate = []
            conference_id = []
            user_id  = []
            confUrl = []
            confStartDate = []
            entryType = []
            for detail in allconf:
                emailIds.append(detail["emailId"])
                city.append(detail["city"])
                country.append(detail["country"])
                imageUrl.append(detail["imageURL"])
                venue.append(detail["venue"])
                state.append(detail["state"])
                confName.append(detail["confName"])
                confStartDate.append(detail["confEndDate"])
                confEndDate.append(detail["confEndDate"])
                user_id.append(detail["user_id"])
                entryType.append(detail["entryType"])
                conference_id.append(detail["conference_id"])
                confUrl.append(detail["confUrl"])
            df = pd.DataFrame({"city":city,"country":country,"imageUrl":imageUrl,"venue":venue,"confName":confName,"entryType":entryType,"state":state,"confStartDate":confStartDate,"confEndDate":confEndDate,"conference_id":conference_id,"user_id":user_id,"confUrl":confUrl})
            ## for good visual we ill use top 5 rows to see
            print("for good looking we ill just visualize the top 5 rows")
            print(df.head())
        if option == 6:
            exit()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
