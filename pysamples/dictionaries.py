
states = {
  "NY": "Newyork",
  "NJ": "New Jersey",
  "IA": "Iowa",
  "PA": "Pennsylvania"
}

print(states)

states["NY"] = "New York"
print(states)

states["CT"] = "Connecticut"
print(states)

print("NY" in states)
print("New York" in states)

for state_code in states:
  print(state_code + ": " + states[state_code])

  