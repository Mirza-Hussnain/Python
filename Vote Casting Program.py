def main():
    print("Welcome to the Voting System!")
    
    vote = input("Do you want to cast a vote? (yes/no): ").lower()
    
    if vote == "yes":
        print("Candidates:")
        print("1. Candidate A")
        print("2. Candidate B")
        print("3. Candidate C")
        print("4. Candidate D")
        
        choice = int(input("Enter the number of the candidate you want to vote for: "))
        
        if 1 <= choice <= 4:
            candidates = ["Candidate A", "Candidate B", "Candidate C", "Candidate D"]
            candidate_name = candidates[choice - 1]
            
            print(f"You have cast your vote for {candidate_name}. Thanks for voting!")
        else:
            print("Invalid candidate number. Your vote has not been cast.")
    elif vote == "no":
        print("Thank you for considering. Have a great day!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
