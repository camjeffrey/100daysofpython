import sys

print("""
         __________
        /\\____;;___\\
       | /         /
       `. ())oo() .
        |\\(%()*^^()^\\
       %| |-%-------|
      % \\ | %  ))   |
      %  \\|%________|
      """
	)
print("Welcome to treasure island.")

print("You awaken on a jungle path, with no memory of how you arrived there. Ahead, the path forks. Do you go 'left' or 'right'?")
direction = input("Do you go 'left' or 'right'? ")
if direction == "right":
      sys.exit("You push through the dense jungle, not seeing the steep drop until it's too late. You step directly off a cliff and fall to your death.")


print("You come across a river. The water doesn't seem to be flowing too fast, but there's no way to tell how deep it is.")
river_choice = input("Do you try to 'swim' across, 'wait' for the water level to drop, or 'build' a raft? ")
if river_choice == "wait":
      sys.exit("Sitting on the bank, oblivious and defenceless, you don't even hear the jaguar creeping up on you before it sinks its teeth into the back of your neck. The fact that you die so quickly is some small mercy.")
elif river_choice == "build":
      sys.exit("When you came up with this idea, you forgot that you don't know anything about constructing watercraft. Halfway across, with your raft sinking and your legs tangled in makeshift rope, you remember. You feel a great sense of embarrassment as you drown.")

print("Dragging yourself up the far bank, panting and exhausted, you see three chests just beyond the treeline.")
chest_choice = input("Do you open the 'left', the 'middle', or the 'right? ")
if chest_choice == "left":
      sys.exit("The lid can't have been raised more than two or three inches by the time the snake strikes your wrist. The veins around the two puncture wounds are already turning black, and you can feel your nerves and muscles shutting down. You have just enough time to wish that you'd drowned back there.")
elif chest_choice == "middle":
      sys.exit("The chest is filled with precious stones, gold coins, and what looks like the Holy Grail. It doesn't change the fact that you're stuck on a strange island with no idea how you got there or how to get home. You're crushed under the realisation of how arbitrary the value of the chest's contents are as you begin the long, slow process of dying on this island.")
else:
      sys.exit("In an equally cruel and nonsenical twist of fate, this old, decaying, golden-age-of-piracy era chest is rigged with a fragmentation grenade. You register, but do not comprehend, the soft metallic clinking of the pin being pulled as you lift the chest's lid, and then it's lights out.")