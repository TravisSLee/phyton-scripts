# Single letter script

data = input("Enter a single letter: ")

if data.islower() == True:
    print('It is a lower case letter.')
else:
    print('It is an uppercase letter.')

#Color script
color = input("Enter a color:" )

color = color.lower()

if color =="red":
    print("The color is red.")
elif color.lower() =="green":
    print("The color is green.")
elif color=="yellow":
    print("The color is yellow.")
else:
    print("Please enter a valid color.")

# State finder script

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


m_states = [s for s in states if "M" in s]

n_states = [s for s in states if "N" in s]

v_states = [s for s in states if "V" in s]
