function ifStatements() {
  let x = 10;
  let y = 13;

  let num = prompt('Enter a number.');

  if (num > 1000) {
    console.log('That\'s a really big number!.');
    if (num > 10000) {
      console.log('That\'s a really really big number!');
    }
  }

  num = prompt('Enter another number.');

  if (num < 0) {
    console.log(num + ' is negative.');
  } else if (num > 0) {
    console.log(num + ' is positive.');
  } else {
    console.log(num + ' is zero.');
  }
}

