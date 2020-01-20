function forLoops() {

  for (var i = 0; i < 10; i++) {
    console.log(i * 10);
  }

  // count from 50 up to 100 (noninclusive) by 5
  for (var i = 50; i < 100; i += 5) {
    console.log(i);
  }

  // print every character in the string 'words' as upper case
  for (var i = 0; i < 'words'.length; i++) {
    console.log('words'[i].toUpperCase());
  }
}
