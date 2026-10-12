# Task - Find topper in physics,math,chem subject 

db = {
    1:[78,97,86],
    2:[97,94,92],
    3:[78,90,87]
}

topper_phy = 0
topper_phy_key = list(db.keys())[0]

topper_math = 0
topper_math_key = list(db.keys())[0]

topper_chem = 0
topper_chem_key = list(db.keys())[0]

for k ,v in db.items():
    if v[0] > topper_phy:
        topper_phy = v[0]
        topper_phy_key = k
    
    if v[1] > topper_math:
        topper_math = v[1]
        topper_math_key = k
    
    if v[2] > topper_chem:
        topper_chem = v[2]
        topper_chem_key = k

print(f"The roll number {topper_phy_key} is the physics topper {topper_phy}")
print(f"The roll number {topper_math_key} is the physics topper {topper_math}")
print(f"The roll number {topper_chem_key} is the physics topper {topper_chem}")



# Crete dictionary of movies - 2026
movies = {
    
        "Border 2": ["Sunny Deol", "Varun Dhawan", "Diljit Dosanjh", "Ahan Shetty", "Sonam Bajwa"],
        "Alpha": ["Alia Bhatt", "Sharvari", "Bobby Deol", "Anil Kapoor"],
        "O Romeo": ["Shahid Kapoor", "Triptii Dimri", "Nana Patekar", "Disha Patani"],
        "Bhooth Bangla": ["Akshay Kumar", "Tabu", "Wamiqa Gabbi", "Paresh Rawal"],
        "Dacoit": ["Adivi Sesh", "Mrunal Thakur", "Anurag Kashyap"],
        "Naagzilla": ["Kartik Aaryan"],
        "Dhamaal 4": ["Ajay Devgn", "Riteish Deshmukh", "Arshad Warsi"],
        "Raftaar": ["Rajkummar Rao", "Keerthy Suresh", "Rajat Kapoor"]
}

print(movies)
