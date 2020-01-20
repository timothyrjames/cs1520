function whileLoops() {
  let i = 0;
  while (i < 10) {
    console.log(i);
    i++;                // JavaScript supports the ++ operator
  }

  while (i >= 0) {
    console.log(i);
    if (i > 2) {
      i /= 2;
    } else {
      i -= 2;
    }
  }
}

  
