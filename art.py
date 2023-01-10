def draw(choice):
    if choice == "rock":
    # Player chose rock , print rock
        return("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    elif choice == "paper":
        # Player chose paper, print paper
        return("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    elif choice == "scissors":
        # Player chose schissors , print schissors
        return("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")