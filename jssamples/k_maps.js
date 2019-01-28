function maps() {
  
  // Map is a new construct in JavaScript; historically
  // people have used plain old objects.

  let states = {
    "NY": "Newyork",
    "NJ": "New Jersey",
    "IA": "Iowa",
    "PA": "Pennsylvania"
  };

  console.log(states);

  states["NY"] = "New York";
  console.log(states);

  states["CT"] = "Connecticut";
  console.log(states);

  // "in" also works in JavaScript
  console.log("NY" in states);
  console.log("New York" in states);

  // note that order here will probably be the order in which these keys
  // were defined.
  for (var stateCode in states) {
    console.log(stateCode + ": " + states[stateCode]);
  }
}  